# Third-party Services

third-party services in your FastAPI application -- e.g., Zapier, SendGrid, and Stripe, to name a few

Most services expose some sort of RESTful API to call or send notifications to your application via webhooks

When implementing a new service, it's important that you don't decrease the overall performance of your web application by blocking the main web process.

>

    The logic introduced in this chapter can be used for any time-consuming work that you'd like handled in the background outside the normal request/response flow.

## Objectives

1. Process form submissions with a Celery worker
2. Handle complicated logic triggered by a webhook notification with a Celery worker
3. Retry a failed Celery task with the retry method

## Problem 1: Blocking Web Process

Say you have an API that lets users subscribe to your newsletter. In the view, you grab the provided email address, and send it to a third-party email marketing API like MailChimp or ConvertKit.

```py
import random

import requests

def subscribe_user(email: str):
    # used for testing a failed api call
    if random.choice([0, 1]):
        raise Exception('random processing error')

    # used for simulating a call to a third-party email marketing api
    requests.post('https://httpbin.org/delay/5')


@users_router.post("/form/")
def subscribe(payload: Body(...)):
    subscribe_user(payload["email"])
    return {"message": "thanks"}

```

So, we have a view which mimics a call to a third-party email marketing API with requests.post('<https://httpbin.org/delay/5>'). This view could degrade performance if you're sustaining heavy traffic.

If you're running three Uvicorn workers with Gunicorn then you'll have three worker processes available to process each HTTP request to that entrypoint. If three users submit at the same time, all three processes might be blocked for at least five seconds.

Since requests is a synchronous library, one solution is to switch to a library that leverages asyncio, such as httpx or aiohttp. But in some cases, the third-party SDK is built without asyncio, so Celery is better option.

## Enter Celery

If you need to call a third-party API within a view, you can move the actual call to an asynchronous Celery task to prevent the web process from being blocked.

Full workflow:

1. You'll want to use JavaScript to hijack the form submission and then send the data to the server via an AJAX request.
2. Within the FastAPI view, enqueue a new task (which takes the submitted email and calls the external API) and return the task ID in the response back to the client.
3. You'll then use that task ID to continue to check the state of the task via another AJAX request.
4. When the task finishes, you should then display the appropriate message based on whether the task succeeds or fails.

> Rather than introducing a polling mechanism (calling the API in a loop, checking the status of the task), you could use WebSockets or HTTP/2 to "push" the response from the server to the client after the task finishes executing

>If you're using an API to process a payment or modify a user submitted file via an external service, then you should definitely use this full workflow.

## Implementation
```py
import logging
import random

import requests
from celery.result import AsyncResult
from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from . import users_router
from .schemas import UserBody
from .tasks import sample_task


logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory="project/users/templates")


def api_call(email: str):
    # used for testing a failed api call
    if random.choice([0, 1]):
        raise Exception("random processing error")

    # used for simulating a call to a third-party api
    requests.post("https://httpbin.org/delay/5")


@users_router.get("/form/")
def form_example_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@users_router.post("/form/")
def form_example_post(user_body: UserBody):
    task = sample_task.delay(user_body.email)
    return JSONResponse({"task_id": task.task_id})


@users_router.get("/task_status/")
def task_status(task_id: str):
    task = AsyncResult(task_id)
    state = task.state

    if state == 'FAILURE':
        error = str(task.result)
        response = {
            'state': state,
            'error': error,
        }
    else:
        response = {
            'state': state,
        }
    return JSONResponse(response)

```

Here, in the form_example_post view, a task called sample_task is enqueued and the task ID is returned. The task_status view can then be used to check the status of the task given the task ID.

We used users_router so the routes will be prefixed with /users:

    /users/form/
    /users/task_status/


```py
@shared_task()
def sample_task(email):
    from project.users.views import api_call

    api_call(email)
```
So, in the sample_task task, the email is passed to the api_call helper. The blocking operation in the helper won't block the web process since it will be handled in the background asynchronously.


```js
<script>
  function updateProgress(yourForm, task_id, btnHtml) {
    fetch(`/users/task_status/?task_id=${task_id}`, {
      method: 'GET',
    })
    .then(response => response.json())
    .then((res) => {
      const taskStatus = res.state;

      if (['SUCCESS', 'FAILURE'].includes(taskStatus)) {
        const msg = yourForm.querySelector('#messages');
        const submitBtn = yourForm.querySelector('button[type="submit"]');

        if (taskStatus === 'SUCCESS') {
          msg.innerHTML = 'job succeeded';
        } else if (taskStatus === 'FAILURE') {
          // display error message on the form
          msg.innerHTML = res.error;
        }

        submitBtn.disabled = false;
        submitBtn.innerHTML = btnHtml;
      } else {
        // the task is still running
        setTimeout(function() {
          updateProgress(yourForm, task_id, btnHtml);
        }, 1000);
      }
    })
    .catch((error) => {
      console.error('Error:', error)
    });
  }

  function serialize(data) {
    let obj = {};
    for (let [key, value] of data) {
      if (obj[key] !== undefined) {
        if (!Array.isArray(obj[key])) {
          obj[key] = [obj[key]];
        }
        obj[key].push(value);
      } else {
        obj[key] = value;
      }
    }
    return obj;
  }

  document.addEventListener("DOMContentLoaded", function() {
    const yourForm = document.getElementById("your-form");
    yourForm.addEventListener("submit", function(event) {
      event.preventDefault();
      const submitBtn = yourForm.querySelector('button[type="submit"]');
      const btnHtml = submitBtn.innerHTML;
      const spinnerHtml = 'Processing...';
      submitBtn.disabled = true;
      submitBtn.innerHTML = spinnerHtml;

      const msg = yourForm.querySelector('#messages');
      msg.innerHTML = '';

      // Get all field data from the form
      let data = new FormData(yourForm);
      // Convert to an object
      let formData = serialize(data);

      fetch('/users/form/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData),
      })
      .then(response => response.json())
      .then((res) => {
        // after we get Celery task id, we start polling
        const task_id = res.task_id;
        updateProgress(yourForm, task_id, btnHtml);
        console.log(res);
      })
      .catch((error) => {
        console.error('Error:', error)
      });
    });
  });
</script>

```

Then, add the core JavaScript to send the initial XHR request to kick off the task along with a request to check the status of the request using the task ID:

What's happening here?

1. On form submit, we disabled the submit button and replaced the button text with "Processing...", to indicate to the end user that some sort of backend processing is happening. We also serialized the form input values and sent them along with the POST request to /users/form/.
2. When a successful response comes back with the task ID, we passed the ID to the updateProgress function, which calls the /users/task_status/ endpoint. updateProgress continues to call that endpoint every second until the task is completed.
3. Once complete, we displayed the appropriate message, updated the text in the button, and enabled the submit button.

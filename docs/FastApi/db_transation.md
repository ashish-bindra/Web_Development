# Database Transactions

how to prevent a Celery task dependent on a SQLAlchemy database transaction from executing before the database commits the transaction.

This is a fairly common issue.

## Objectives

- Describe what a database transaction is and how to use it in SQLAlchemy
- Prevent a task from executing before the database commits a transaction

## What is a Database Transaction?

A database transaction is a unit of work that is either committed (applied to the database) or rolled back (undone from the database) as a unit.

Most databases use the following pattern:

1. Begin the transaction.
2. Execute a set of data manipulations and/or queries.
3. If no error occurs, then commit the transaction.
4. If an error occurs, then roll back the transaction.

a transaction is a very useful way to keep your data far away from chaos.

## Database Transactions in SQLAlchemy

To run web container

```sh
docker compose exec web bash
root@0da5a3df5bfb:/app# python
Python 3.11.4 (main, Jun 13 2023, 15:34:37) [GCC 8.3.0] on linux

```

Then, enter the following:

```py
from main import app
from app.database import SessionLocal
session = SessionLocal()
from app.users.models import User

username = 'michael_test_1'
# user = User(username=f'{username}', email=f'{username}@test.com')
user = User(username=f'{username}', user_email=f'{username}@test.com',user_password=username)

```

### State Management

It’s helpful to know the states which an instance can have within a session:

- Transient - an instance that’s not in a session, and is not saved to the database; i.e. it has no database identity. The only relationship such an object has to the ORM is that its class has a Mapper associated with it

- Pending - when you Session.add() a transient instance, it becomes pending. It still wasn’t actually flushed to the database yet, but it will be when the next flush occurs.

- Persistent - An instance which is present in the session and has a record in the database.

- Deleted - An instance which has been deleted within a flush, but the transaction has not yet completed.

- Detached - an instance which corresponds, or previously corresponded, to a record in the database, but is not currently in any session

```py
from sqlalchemy import inspect
insp = inspect(my_object)
insp.persistent
```

Let's look at the different states a SQLAlchemy database instance can be in.

```py
from sqlalchemy import inspect
insp = inspect(user)
insp.transient # True

insp.persistent # False
print(user.id) # None

```

It's currently in a transient state, so it's not part of a session yet.

Note: Multiple transactions can be tied to a single session.

Add it to a session, which will move the state to pending:

```py
session.add(user)

insp.transient # False
insp.pending # True
print(user.id) # None
```

To create a database record, call flush to move the state to persistent:

```py
session.flush()

insp.transient # False
insp.pending   # False
insp.persistent # True
print(user.id) # 1
```

At this point, you now have a user ID. That said, the data has not been inserted yet. To verify this, open a new terminal window and run:

```sh
docker compose exec db sh
psql -U fastapi_celery fastapi_celery

psql (16.9)
Type "help" for help.

fastapi_celery=# select * from users;
 id | username | user_email | user_password 
----+----------+------------+---------------
(0 rows)

fastapi_celery=#

```

To commit the changes, run:

```sh
session.commit()
```

Verify

```sh
fastapi_celery=# select * from users;
\ id |    username    |       user_email        | user_password  
----+----------------+-------------------------+----------------
  1 | michael_test_1 | michael_test_1@test.com | michael_test_1
(1 row)
```

Notes:

1. `flush` communicates a series of operations to the database. The database maintains them as pending operations.
2. The changes aren't persisted permanently to disk until `commit` is called.
3. `commit` calls `flush` beforehand, so you don't need to explicitly call flush.

## Managing Transactions

**It's recommended to use the following pattern to wrap the database operation code:**

```py
username = 'michael_test_1'
user = User(
    username=f'{username}',
    email=f'{username}@test.com',
)

with session.begin():
    session.add(user)

# commits transaction at the end, or rolls back if there was an exception raised
```

If an exception is raised (primary key, foreign key, or "not nullable" constraint violations), rollback is called to fully reset the state of the session back to transient.

Or you can use this pattern:

```py
try:
    username = 'michael_test_1'
    user = User(
        username=f'{username}',
        email=f'{username}@test.com',
    )
    session.add(user)
    session.commit()
except Exception as e:
    session.rollback()
    raise
```

Notes:

1. In old versions of SQLAlchemy, you had to explicitly call rollback in the except block.
2. In newer versions, session.begin() helps us keep the code clean.

## Enqueue Reference

In situations where a Celery task needs to work with data from a database, you should always (if possible) enqueue a reference to the data rather than the data itself. For example, rather than adding an email address, which could change before the task runs, add the user's primary database key.

From the Celery docs:

Another gotcha is Django model objects. They shouldn’t be passed on as arguments to tasks. It’s almost always better to re-fetch the object from the database when the task is running instead, as using old data may lead to race conditions.

```py
@users_router.get("/transaction_celery/")
def transaction_celery(session: Session = Depends(get_db_session)):
    username = random_username()
    user = User(
        username=f'{username}',
        email=f'{username}@test.com',
    )
    with session.begin():
        session.add(user)

    print(f'user {user.id} {user.username} is persistent now')
    
    task_send_welcome_email.delay(user.id)
    return {"message": "done"}

```

1. With session: `Session = Depends(get_db_session)`, the `session` is the yield value of the `get_db_session`. Here, we leveraged FastAPI's dependency injection system.
2. With `db_context = contextmanager(get_db_session)`, we used the database session with Celery in clean way. We'll look more at this shortly.
3. The `transaction_celery` view creates a random user and saves it to the database.
4. If the database operation fails, `session.rollback` will run and an exception will be raised.
5. A new task is only enqueued if the database operation is successful. Notice how we passed a reference to the data -- e.g., `user.id` -- rather than the email itself.

> Alternatively, you could use a random username generator for testing purposes like Faker.

```
Add the task to project/users/tasks.py:

@shared_task()
def task_send_welcome_email(user_pk):
    from project.users.models import User

    with db_context() as session:
        user = session.get(User, user_pk)
        logger.info(f'send email to {user.email} {user.id}')

```

1. with db_context() as session, we can use the session to interact with database in Celery now. And the session will be closed after we exit the context. You can check Python contextlib.contextmanager to learn more.
2. Here, with the user reference, we grabbed the user instance, which we then used to send a welcome email message to.

> Yes, we don't actually send the email. Do this on your own if you'd like.

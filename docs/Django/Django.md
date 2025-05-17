# Django

## User Authentication and Authorization
- Authentication: The process of validating user is called authentication.
- Authorization: The process of validating access permissions of user is called authorization.

Django provides the following 2 in built applications for user authentication.

1. django.contrib.auth
2. django.contrib.contenttypes

Django uses PBKDF2_Sha256 algorithm to encrypt passwords and hence passwords won't be stored in plain text form and we can expect more security. Even superuser also cannot see any user's password.

Based on our requirement, we can use more secure hashing algorithms also like bcrypt and argon2. We can install with pip as follows.
- `pip install bcrypt`
- `pip install django[argon2]`

More secured algorithm is argon2 and then bcrypt followed PBKDF2.
In settings.py we have to configure password hashers as follows.
    
     PASSWORD_HASHERS=[ 
     'django.contrib.auth.hashers.Argon2PasswordHasher', 
     'django.contrib.auth.hashers.BCryptSHA256PasswordHasher', 
     'django.contrib.auth.hashers.BCryptPasswordHasher', 
     'django.contrib.auth.hashers.PBKDF2PasswordHasher',
     'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher', 
     ]
    
Django will always consider from first to last. ie order is important.
Just like templates and static folder, we have to create media folder also.


Difference between Static and Media Folders: 

☕ Static folder contains images, CSS files etc which are provided by application to the end user. 

☕ But media folder contains the resources like images provided by end user to the application (like profile image etc)

How to Configure Media Folder in settings.py File: 
```py
MEDIA_DIR = os.path.join(BASE_DIR,'media') MEDIA_ROOT = MEDIA_DIR MEDIA_URL = '/media/'

from django.contrib.auth.decorators import login_required
@login_required def java_exams_view(request): return render(request,'testapp/java.html')
```
If we use @login_required decorator for any view function,then auth application will check whether user login or not. If the user not login then the control will be forwarded to login page.
http://127.0.0.1:8000/accou

LOGOUT_REDIRECT_URL='/'
But we can configure our own target page after login inside settings.py as follows.
LOGIN_REDIRECT_URL='/'


Future Assignments: 
1. How to customize our own login form
2. How to use auth application provided default signup form 
3. Social Login


## CBV
```py
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "authApp/login.html"

    def get_success_url(self):
        return self.get_redirect_url() or "/authApp/dashboard/"
```

```py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get("next", "/authApp/dashboard/")  # Redirect to 'next' or default
            return redirect(next_url)
    return render(request, "authApp/login.html")

```
from django.contrib.auth.views import LoginView

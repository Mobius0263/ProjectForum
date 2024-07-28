Update 4:
- MAIN/ProjectForum/settings.py (TinyMCE default added, Line 134)
- MAIN/main/apps.py
- MAIN/main/models.py (Added email)
- MAIN/main/signals.py (Added)
- MAIN/main/views.py
- MAIN/register/forms.py (Added CustomUserCreationForm)
- MAIN/register/views.py (Changed signup function)
- MAIN/static/css/style.css (Minor color change)
- MAIN/templates/base.html (Show username and profile pic)
- MAIN/templates/create_post.html (Added TinyMCE text editor)
- MAIN/templates/detail.html (Added date of creation, changed username and fullname, changed comment textbox to TinyMCE text editor)
- MAIN/templates/forums.html (Changed fullname to username)
- MAIN/templates/latest-posts.html (Minor typo fix, changed fullname to username)
- MAIN/templates/posts.html (Changed fullname to username)
- MAIN/templates/search.html(Changed fullname to username)
- MAIN/templates/register/signup.html (Added error message)

Updates 3:
- Added comments for all important .py files
- Added comments for MAIN/main/static/js/main.js

Updates 2:
- Added update profile into MAIN/main/templates/base.html
- removed MAIN/main/templates/home.html

Updates 1:
- MAIN/main/forms.py
- MAIN/main/models.py
- MAIN/main/views.py
- MAIN/register/views.py
- MAIN/static/css/style.css
- MAIN/templates/base.html
- MAIN/templates/create_post.html
- MAIN/templates/detail.html
- MAIN/templates/posts.html
- MAIN/templates/register/update.html

Clone repository:
```
git clone https://github.com/Mobius0263/ProjectForum.git
```

In MAIN, open git bash here:
```
code .
```

Open Terminal in VSCode:
```
python -m pip install -r requirements.txt
```

Run server:
```
python manage.py runserver
```

Admin site:
```
http://127.0.0.1:8000/admin/
```

# Library Management System

A Django-based web application for managing library operations, including book cataloging, user accounts, notices, and maps integration.

## Features

- User authentication and accounts
- Book management system
- Notice board for announcements
- Interactive maps
- REST API with JWT authentication
- Email notifications

## Setup Instructions

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd LibraryManagementSystem
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**

   Create a `.env` file in the project root and add the following variables:

   ```env
   SECRET_KEY=your_django_secret_key_here
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_email_app_password
   DEBUG=True
   ```

   **Note:** Never commit the `.env` file to version control. It's already included in `.gitignore`.

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure

```
LibraryManagementSystem/
├── accounts/          # User authentication app
├── books/            # Book management app
├── noticeBoard/      # Notice board app
├── maps/             # Maps integration app
├── static/           # Static files
├── templates/        # HTML templates
├── manage.py         # Django management script
└── LibraryManagementSystem/  # Main project settings
```

## API Endpoints

The application includes REST API endpoints for:

- User registration and authentication
- Book CRUD operations
- Notice management

API documentation available at `/api/` when running the server.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

---

## Django + Bootstrap Carousel Debug Summary

## What Went Wrong

| Problem | Description |
|--------|-------------|
| **Incorrect app name** | Used `'django_bootstrap5'` instead of `'django_bootstrap_v5'` in `INSTALLED_APPS`. |
| **Template tag mismatch** | Used `{% load django_bootstrap5 %}` instead of `{% load django_bootstrap_v5 %}`. |
| **Static tag error** | Used `{% static %}` without `{% load static %}` at the top of the template. |
| **Mixed Bootstrap methods** | Combined Django plugin-based Bootstrap with CDN-based Bootstrap, causing confusion. |
| **Inconsistent image sizes** | Carousel images had different dimensions, leading to layout issues. |

---

## How You Fixed It

| Fix | Action |
|-----|--------|
| Uninstalled plugin | Removed `django-bootstrap-v5` using `pip uninstall` and deleted from `INSTALLED_APPS`. |
| Switched to CDN | Used Bootstrap 5 via CDN for simplicity and speed. |
| Loaded static tag | Added `{% load static %}` at the top of your template. |
| Unified image sizes | Added `.carousel-image` class with `height: 500px` and `object-fit: cover`. |
| Cleaned template | Removed unused attributes and simplified HTML structure. |

---

## 🎯 Final Carousel Setup Highlights

```html
<!-- Inside <head> -->
<style>
  .carousel-image {
    height: 500px;
    object-fit: cover;
  }
</style>

<!-- Inside carousel -->
<img
  src="{% static 'images/naruto1.jpg' %}"
  class="d-block w-100 carousel-image"
  alt="Naruto 1"
/>
## 🧠 Pro Tips

- Use `{% load static %}` in every template that uses `{% static %}`.
- Prefer CDN for Bootstrap unless you need offline or custom builds.
- Use `object-fit: cover` to maintain image proportions and fill space evenly.
<!------------------------------------------------------------------>

## 🛠️ Django TemplateSyntaxError Summary

### ❌ Error Message

'%' is not a registered tag library. Must be one of:
admin_list, admin_modify, admin_urls, cache, i18n, l10n, log, static, tz



### 📍 Location
- **Template file**: `home.html`
- **Error line**: Line 3
- **Problematic code**:
  ```django
  {% load static % }
  ```

### ✅ Root Cause

- Extra space before the closing `%}` in `{% load static % }`
- Django fails to recognize the tag due to incorrect syntax

### ✅ Correct Syntax

```django
{% load static %}
```

### ✅ Full Fixed Line Example

```django
{% extends 'base.html' %}
{% load static %}
{% block content %}
{% comment %}
```

### 🧠 Pro Tip

Always double-check:

- `{% load %}` syntax (no extra spaces)
- `{% block %}`, `{% endblock %}` structure
- `{% comment %} ... {% endcomment %}` usage

-------------------------------------------------------------------------------------------------------------

# 🛠️ Django 404 Handling Summary

## 🔎 What is a 404?

- A **404 error** means "Page Not Found" — the requested URL doesn’t match any defined route.
- Django provides two main ways to customize how 404s are displayed.

---

## 📌 Methods of Handling 404

### 1. Static Template (`404.html`)

- Place a file named `404.html` inside your `templates/` directory.
- Django automatically renders it when:
  - `DEBUG = False`
  - No matching URL is found
- Simple and quick, but limited to static content.

```html
<!-- templates/404.html -->
<h2>Oops! Page Not Found</h2>
<p>The page you’re looking for doesn’t exist.</p>
<a href="/">Back to Home</a>
------------------------------------------------------------------------------------------------------------
# Django Static Files & Custom 404 Issue (DEBUG=False)

## Problem

When `DEBUG = False` in a Django project:
- Images, CSS, and JavaScript do not load
- Custom `404.html` page appears without styling
- Same project works when `DEBUG = True`

---

## Cause

Django serves static files automatically **only in development**.  
In production (`DEBUG = False`), Django requires explicit static file handling.

---

## Development Solution (DEBUG=True)

### settings.py

```python
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### urls.py (development only)

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

**Result:**  
Static files work locally. Not suitable for production.

---

## Production Solution Using WhiteNoise (DEBUG=False)

### 1. Install WhiteNoise

```bash
pip install whitenoise
```

### 2. Add Middleware

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
```

### 3. Static Configuration

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### 4. Enable WhiteNoise Storage

```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 5. Collect Static Files

```bash
python manage.py collectstatic
```

---

## What `CompressedManifestStaticFilesStorage` Does

```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Usage in Code

- Used during `collectstatic`
- Generates hashed filenames  
  Example: `style.css → style.83hd9f.css`
- Used by `{% static %}` template tag
- Used by WhiteNoise to serve files

### Why It Is Needed

- Compresses static files (gzip/brotli)
- Prevents browser cache issues
- Improves load speed
- Required for production-grade deployments

---

## Custom 404 Configuration

### views.py

```python
def handler404(request, exception):
    return render(request, '404.html', status=404)
```

### project urls.py

```python
handler404 = 'LibraryManagementSystem.views.handler404'
```

### 404.html

```html
{% load static %}
<img src="{% static 'images/404.png' %}" alt="404">
```

---

## Final Result

- Static files load when `DEBUG=False`
- Custom 404 page works correctly
- No Nginx/Apache required
- Production ready

---

## One-Line Summary

When `DEBUG=False`, Django stops serving static files; using `STATIC_ROOT`, `collectstatic`, and WhiteNoise with compressed manifest storage fixes missing images and broken custom error pages.

----------------------------------------------------------------------------------------------------------------------------------------------

# Django Email Sending (send_mail → EmailMessage)

This file documents how email sending was implemented in Django, common mistakes faced, and the final correct solution with CC, BCC, and attachments.

---

## 1. send_mail() – Initial Attempt

### ❌ Wrong Usage

```python
send_mail(
    subject="Hello",
    body="Test email",
    from_email="noreply@domain.com",
    to=["test@example.com"]
)
```

**Error**

```
TypeError: send_mail() got an unexpected keyword argument 'to'


```

# Quick Rule of Thumb

Use send_mail() → message + recipient_list

Use EmailMessage → body + to

### ✅ Correct Usage

```python
send_mail(
    subject="Hello",
    message="Test email",
    from_email="noreply@domain.com",
    recipient_list=["test@example.com"]
)
```

---

## 2. Why EmailMessage?

`send_mail()` supports only simple emails.  
For **CC, BCC, attachments**, Django recommends `EmailMessage`.

---

## 3. EmailMessage with CC & BCC

```python
from django.core.mail import EmailMessage

email = EmailMessage(
    subject="Hello from Django",
    body="Test email with CC and BCC",
    from_email="noreply@domain.com",
    to=["main@example.com"],
    cc=["copy@example.com"],
    bcc=["hidden@example.com"]
)

email.send()
```

---

## 4. Common Errors & Fixes

### ❌ MIMEPart.**init** error

**Cause:** Used Python `email.mime`  
**Fix:** Always import from Django

```python
from django.core.mail import EmailMessage
```

---

### ❌ attach_file not found

**Cause:** Imported Python’s `email` module  
**Fix:** Use Django’s EmailMessage

---

### ❌ NameError: email not defined

**Fix**

```python
email = EmailMessage(...)
email.attach_file("path/to/file")
```

---

## 5. Attachments (Correct Way)

### ❌ Wrong

```python
email.attach_file("media/images/file.png")
```

### ✅ Correct

```python
import os
from django.conf import settings

file_path = os.path.join(settings.MEDIA_ROOT, "images", "file.png")
if os.path.exists(file_path):
    email.attach_file(file_path)
```

---

## 6. Project Structure (Example)

```
LibraryManagementSystem/
├── media/
│   └── images/
│       └── file.png
├── manage.py
```

---

## 7. Final Working Django View

```python
from django.core.mail import EmailMessage
from django.http import HttpResponse
import os
from django.conf import settings

def send_test_email(request):
    email = EmailMessage(
        subject="Hello from Django",
        body="Email with CC, BCC and attachment",
        from_email="noreply@domain.com",
        to=["test@example.com"],
        cc=["copy@example.com"],
        bcc=["hidden@example.com"]
    )

    file_path = os.path.join(settings.MEDIA_ROOT, "images", "file.png")
    if os.path.exists(file_path):
        email.attach_file(file_path)

    email.send()
    return HttpResponse("Email Sent Successfully")
```

---

## Key Points

- `send_mail()` → simple emails only
- `EmailMessage` → CC, BCC, attachments
- Always use `django.core.mail`
- Use `MEDIA_ROOT` for attachments
- Check file existence before attaching

-------------------------------------------------------------------------------------------
Django Generic Views

📖 Summary

Django Generic Views are pre-built class-based views (CBVs) that simplify common web development tasks. Instead of writing repetitive function-based views (FBVs), you can use these ready-made classes to handle CRUD operations and data display with minimal code.

Generic Views are designed to:

Reduce boilerplate code

Provide consistency across projects

Offer extensibility through method overrides

Speed up development for common patterns

🔑 Key Generic Views

ListView → Display a list of objects

DetailView → Show details of a single object

CreateView → Add a new object

UpdateView → Edit an existing object

DeleteView → Remove an object

📝 Example

from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"

# urls.py

from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]

CRUD & large projects

🎯 Learning Points

FBVs are great for beginners and unique workflows.

Generic Views shine in repetitive tasks like CRUD.

Both can be mixed in the same project.

Industry projects often combine FBVs for clarity and CBVs for efficiency.

✅ Best Practice

Start learning with FBVs to understand Django basics.

Move to Generic Views for efficiency once comfortable.

Use ModelForms + Generic Views for powerful CRUD APIs.

🚀 Conclusion

Generic Views are not a replacement for FBVs but a complement. They help developers write cleaner, faster, and more maintainable code while still allowing customization when needed.

--------------------------------------------------------------------------------------------

# Django Form Data Not Saving – Summary

## 📌 Issue Faced

While using a **Django Form** (`MessageForm`), the form was:

- Accepting user input
- Validating data correctly

But ❌ **data was NOT saved in the database** and did not appear in the Django Admin panel.

---

## ❓ Why This Happened

- A normal **Django Form** is **NOT connected to any database model**.
- Django does not know **which table** the form data should be saved into.
- Therefore:
  - Form → input + validation only
  - No automatic database save

---

## ✅ Correct Understanding

- **Form**
  - Handles input
  - Validates data
  - ❌ Does NOT save data automatically

- To save data:
  - You must create a **Model**
  - Then manually insert data using `form.cleaned_data`

---

## 💾 Manual Save Solution (Form → Model → Database)

### Model

```python
from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
````

### View (Manual Save)

```python
from .models import Message

def message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return render(request, 'home/success.html')
    else:
        form = MessageForm()
    return render(request, 'home/message.html', {'form': form})
```

✔ Data is now saved in the database
✔ Data is visible in Django Admin

---

## 🔑 Final Summary

- ✅ **Django Form**
  → Input + Validation only
  → Database save must be done manually

- ✅ To save Form data:

  - Create a Model
  - Use `form.cleaned_data`
  - Call `Model.objects.create(...)`

- 🚀 Shortcut:

  - Use **ModelForm**
  - Just call `form.save()`

---

### 📌 One-Line Conclusion

> Django `Form` does not save data by default — saving requires a Model and manual database logic, or switching to `ModelForm`.

----------------------------------------------------------------------------------------------------
# Django URL Name Error (NoReverseMatch) – Summary

## 📌 Issue Faced

In the Django project, a navigation link in the template was not working and raised a
**NoReverseMatch** error.
🔑 Key Learnings

{% url 'name' %} works only if a URL with that name exists

URL name and {% url %} must match exactly

path('', ...) still needs a proper name if used in templates

One app can have multiple named routes under the same prefix
---------------------------------------------------------------

{{ form.as_p }} is a shortcut that renders each Django form field wrapped in <p> tags, making forms quick to display and neatly formatted in templates.

-------------------------------------------------------------------


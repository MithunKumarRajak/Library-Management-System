# Library-Management-System

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

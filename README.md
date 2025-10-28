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


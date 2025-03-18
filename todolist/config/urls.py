from django.contrib import admin
from django.urls import path, include

### localhost:8000/api/v1/
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("todo.urls"))]

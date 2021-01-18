from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('jutsu/', include('jutsu.urls')),
    path('admin/', admin.site.urls),
]
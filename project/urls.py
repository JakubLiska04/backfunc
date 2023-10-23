from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('live_statistic_app.urls')),
    path('admin/', admin.site.urls),
]

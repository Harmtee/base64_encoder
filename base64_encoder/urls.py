from django.contrib import admin
from django.urls import path, include

from api.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

from django.contrib import admin
from django_private_chat import urls as django_private_chat_urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('django_private_chat.urls')),
]

from django.contrib import admin
from django.urls import path, include
from Core.urls import urlpatternsCore
from UserProfile.urls import urlpatternsUserProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatternsCore)),
    path('', include(urlpatternsUserProfile))
]
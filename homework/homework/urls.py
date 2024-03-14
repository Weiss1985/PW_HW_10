
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("quotes.urls")),
    path('author/', include("authors.urls")),
    path('tag/', include("tags.urls")),
    path('users/', include("users.urls")),

]

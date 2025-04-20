
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('wiki/', include('wiki.urls')),
    path('auth/', include('authentication.urls'))
]

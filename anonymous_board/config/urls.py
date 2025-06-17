from django.contrib import admin
from django.urls import path, include  # ← include 추가!


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('board.urls')),
]

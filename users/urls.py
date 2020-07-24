from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import profile_view,signup_view,login_view,logout_view,upload_pic


urlpatterns = [
    path('profile/', profile_view),
    path('signup/', signup_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('upload/', upload_pic)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
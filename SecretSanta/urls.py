from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from users.views import UserView

router = DefaultRouter()
router.register(r'santas', UserView, base_name='santas')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]

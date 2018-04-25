from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from eMenu import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'menus', views.MenuViewSet)
router.register(r'dishes', views.DishesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.MenuList),
    path('insert_sample_data', views.insert_sample_data)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



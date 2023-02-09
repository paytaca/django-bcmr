from rest_framework import routers

from main import views


app_name = "main"

router = routers.DefaultRouter()

router.register("registries", views.RegistryViewSet)
router.register("tokens", views.TokenViewSet)

urlpatterns = router.urls

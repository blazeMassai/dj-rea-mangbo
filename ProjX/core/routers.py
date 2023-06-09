from rest_framework import routers

from core.auth.viewsets import LoginViewSet, RefreshViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()

# ##################################################################### #
# ###################USER ###################### #
# ##################################################################### #

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

urlpatterns = [
    *router.urls
]
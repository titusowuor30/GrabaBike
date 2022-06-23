from rest_framework.routers import DefaultRouter
#from .apiviews import PollViewSet

from django.urls import path
from . views import *

router = DefaultRouter()
router.register('listusers', UserViewSet)
router.register('riders', RiderViewSet)
router.register('rides', RidesViewSet)
router.register('transactions', TransactionsViewSet)
router.register('roles', RolesViewSet)

urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path('riders/add', RideCreate.as_view()),
    path('rides/add', RideCreate.as_view()),
    path('transactions/add', TransactionsCreate.as_view()),
    path('roles/add', RolesCreate.as_view()),
    path('rides/confirm_ride/', confirm_rides),
    path('rides/complete_ride/', complete_rides),
]
urlpatterns += router.urls

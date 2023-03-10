from django.urls import path
from .views.user_views import Signup, Login, Logout
from .views.spot_views import Spots

urlpatterns = [
    path('sign-up/', Signup.as_view(), name='sign-up'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('spots/', Spots.as_view(), name='spots'),
]
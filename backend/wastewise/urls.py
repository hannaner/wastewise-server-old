from django.urls import path
from .views.user_views import Signup, Login, Logout
from .views.spot_views import SpotsView, SpotDetailView
from .views.item_views import ItemsView, ItemDetailView

urlpatterns = [
    path('sign-up/', Signup.as_view(), name='sign-up'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('spots/', SpotsView.as_view(), name='spots'),
    path('spots/<int:pk>', SpotDetailView.as_view(), name='spots'),
    path('items/', ItemsView.as_view(), name='items'),
    path('items/<int:pk>', ItemDetailView.as_view(), name='items'),
]
from django.urls import path

from .views import SignUpView
from .views import (
    login_view,
    logout_view,
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

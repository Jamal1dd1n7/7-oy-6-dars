from django.urls import path
from .views import *

urlpatterns = [
    # URL with Generic views:
    # Home
    path('', HomeView.as_view(), name='home'),
    # ----------------------------------------------------------------------------------------------------------------------------------------------------

]
from django.urls import path
#from .views import EventRegistrationView, EventRegistrationDetailView
from .views import EventRegistrationListCreateView, EventRegistrationDetailView
from .views import UserRegistrationView
from .views import CustomLoginView


urlpatterns = [
    #path('register/', EventRegistrationView.as_view(), name='event-register'),
    #path('register/<int:pk>/', EventRegistrationDetailView.as_view(), name='event-detail'),
    path('register/', EventRegistrationListCreateView.as_view(), name='event-list-create'),
    path('register/<int:pk>/', EventRegistrationDetailView.as_view(), name='event-detail'),
    path('register-user/', UserRegistrationView.as_view(), name='register-user'),
    
    #Create Custom Login API (Optional Improvement)
    path('login/', CustomLoginView.as_view(), name='custom-login'),

]




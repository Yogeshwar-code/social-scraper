from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions #, permissions (Only admin can delete)
from .models import EventRegistration
from .serializers import EventRegistrationSerializer
#Filter and search
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from .serializers import LoginSerializer


"""
# EventRegistrationView (GET all + POST)
# EventRegistrationDetailView (GET by ID + PUT + DELETE)
class EventRegistrationView(APIView):

    # GET → Fetch all registrations
    def get(self, request):
        registrations = EventRegistration.objects.all()
        serializer = EventRegistrationSerializer(registrations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST → Create new registration
    def post(self, request):
        serializer = EventRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Event Registration Successful"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EventRegistrationDetailView(APIView):

    def get(self, request, pk):
        registration = get_object_or_404(EventRegistration, pk=pk)
        serializer = EventRegistrationSerializer(registration)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def put(self, request, pk):
        registration = get_object_or_404(EventRegistration, pk=pk)
        serializer = EventRegistrationSerializer(registration, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Registration updated successfully"},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        registration = get_object_or_404(EventRegistration, pk=pk)
        registration.delete()
        return Response(
            {"message": "Registration deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
"""

# 1 ListCreateAPIView
# 2 RetrieveUpdateDestroyAPIView

#These automatically handle CRUD.

# GET (all) + POST
class EventRegistrationListCreateView(generics.ListCreateAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer

    #newly added three lines for filtering process
    # Filtering fields
    filterset_fields = ['event_name']

    # Search fields
    search_fields = ['name', 'email']

    # Ordering fields
    ordering_fields = ['name', 'id', 'registered_at']

# GET (by id) + PUT + DELETE
class EventRegistrationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer

    #(Only admin can delete) logic function DELETE → Only admin allowed
    # Other methods → Any authenticated user allowed This is dynamic permission control.
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class CustomLoginView(APIView):
    permission_classes = []  # No authentication required

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
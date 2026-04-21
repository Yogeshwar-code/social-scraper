"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
#from django.http import HttpResponse      #by using Render, open admin url on browser and admin logging
#from django.contrib.auth import get_user_model  #by using Render, open admin url on browser and admin logging
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Define schema_view FIRST
schema_view = get_schema_view(
    openapi.Info(
        title="Event Registration API",
        default_version='v1',
        description="API documentation for Event Registration Project",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[], #we are using:  JWT Authentication , Not Basic Authentication
    #So we must tell Swagger:  "Use Bearer Token instead of Basic Auth"
)

"""
#by using Render, open admin url on browser and admin logging
def create_admin(request):
    User = get_user_model()
    if not User.objects.filter(username="Yogesh").exists():
        User.objects.create_superuser(
            "Yogesh",
            "yogesh@gmail.com",
            "yogesh@123"
        )
        return HttpResponse("Superuser created")
    return HttpResponse("Already exists")
"""
# then urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/scraper/', include('scraper.urls')),
    path('api/events/', include('events.urls')),

    # path("create-admin/", create_admin),    #by using Render, open admin url on browser and admin logging  

    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   
]



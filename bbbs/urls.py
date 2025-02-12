"""bbbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt import views as jwt_views

from bbbs.afisha.views import EventList, EventParticipantList
from bbbs.questions.views import QuestiosList
from bbbs.common.views import CityList, ProfileView, TagList
from bbbs.main.views import MainView
from bbbs.places.views import PlaceList
from bbbs.rights.views import RightList

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/tags/', TagList.as_view()),
    path('api/v1/questions/', QuestiosList.as_view()),
    path('api/v1/cities/', CityList.as_view()),
    path('api/v1/profile/', ProfileView.as_view()),
    path('api/v1/main/', MainView.as_view()),
    path('api/v1/afisha/events/', EventList.as_view()),
    path('api/v1/afisha/event-participants/', EventParticipantList.as_view()),
    path('api/v1/places/', PlaceList.as_view()),
    path('api/v1/rights/', RightList.as_view()),
]

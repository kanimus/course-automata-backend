from django.urls import path, include
from apps.user.views import (
    LoginView,
    LogoutView,
    ConfigSettingsView,
    UserPatternsView,
    GetSchoolDataView
)


urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('schools/config', ConfigSettingsView.as_view()),
    path('schools/pattern', UserPatternsView.as_view()),
    path('schools', GetSchoolDataView.as_view())
]
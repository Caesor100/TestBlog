from django.urls import path
from .views import UserProfile, UserProfiles, UserList, TotalUsers


app_name = "users"
urlpatterns = [
    path('total-users/', TotalUsers.as_view()),
    path('user-list/', UserList.as_view()),
    path('user-profiles/', UserProfiles.as_view()),
    path('user-profile/<int:pk>', UserProfile.as_view())
]

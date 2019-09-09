from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserOurRegistration

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserProfileSerializer, UserNameSerializer

from .models import User


class UserProfiles(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response({'users': serializer.data})


class UserProfile(APIView):
    def get(self, request, pk):
        users = User.objects.filter(pk=pk)
        serializer = UserProfileSerializer(users, many=True)
        return Response({'user': serializer.data})


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserNameSerializer(users, many=True)
        return Response({'users': serializer.data})


class TotalUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response({'total-users': len(users)})


def register(request):
    if request.method == "POST":
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} was successfully created, enter a name \
            user and password for successful authorization')
            return redirect('user')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Registration'})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

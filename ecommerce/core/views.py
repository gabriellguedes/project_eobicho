from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


def login(request):
	return HttpResponseRedirect(reverse('contas:login'))



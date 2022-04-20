from asyncio import get_event_loop_policy
import imp
import random
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from myproject.settings import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from io import *
from xhtml2pdf import pisa

# Create your views here.





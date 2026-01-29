from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.db import OperationalError, transaction, IntegrityError
from rest_framework_simplejwt.authentication import JWTAuthentication
import json

from presenze.models import Presenza
from partecipanti.models import Partecipante
from giorni_presenze.models import Giorno



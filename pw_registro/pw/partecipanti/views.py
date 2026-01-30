from django.http import JsonResponse
from django.db import OperationalError
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

from .models import Partecipante
from presenze.models import Presenza 
from giorni_presenze.models import Giorno

# VISTA DEGLI ADMIN

@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def manage_participants(request):
    """
    LOGICA ADMIN:
    GET -> Vede la lista di tutti i partecipanti con matricola UUID.
    POST -> Inserisce un nuovo partecipante (email e data) per autorizzarlo.
    """
    if not request.user.is_admin:
        return JsonResponse({'error': 'Solo l\'admin può gestire i partecipanti'}, status=403)

    if request.method == 'GET':
        partecipanti = Partecipante.objects.all()
        # ... (logica di prima per creare la lista)
        return JsonResponse(list, safe=False)

    if request.method == 'POST':
        # ... (logica di prima per creare il partecipante)
        return JsonResponse({'status': 'creato'}, status=201)

# VISTA DEI PARTECIPANTI

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_my_attendance_summary(request):
    """
    Calcola la percentuale basata sui giorni totali e le presenze effettive
    """
    try:
        # 1. Recuperiamo il partecipante collegato all'utente loggato
        partecipante = Partecipante.objects.get(user=request.user)

        #Contiamo quanti giorni di lezione totali esistono nel database
        giorni_totali = Giorno.objects.count()

        #Contiamo quante volte il partecipante è segnato con stato=True
        presenze_effettive = Presenza.objects.filter(
            partecipante=partecipante, 
            stato=True
        ).count()

#Calcolo percentuale dinamico
        percentuale = (presenze_effettive / giorni_totali * 100) if giorni_totali > 0 else 0

        return JsonResponse({
            'matricola': partecipante.matricola,
            'dati_frequenza': {
                'lezioni_totali': giorni_totali,
                'presenze_confermate': presenze_effettive,
                'percentuale': f"{round(percentuale, 2)}%",
                'obiettivo_80_percento': percentuale >= 80
            }
        }, status=status.HTTP_200_OK)

    except Partecipante.DoesNotExist:
        return JsonResponse({'error': 'Profilo non trovato'}, status=404)
    except OperationalError:
        return JsonResponse({'error': 'Database non raggiungibile'}, status=503)
    





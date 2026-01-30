from rest_framework import serializers
from .models import Partecipante

class ParticipantAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partecipante
        # L'admin inserisce solo l'email e il nome
        fields = ['id', 'matricola', 'nome_completo', 'email_pre_autorizzata', 'data_iscrizione']
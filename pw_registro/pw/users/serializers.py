from rest_framework import serializers
from django.contrib.auth import get_user_model
from partecipanti.models import Partecipante

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']


    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Le password non coincidono'})
        # controllo via di mezzo. L'email deve essere già stata censita dall'admin
        if not Partecipante.objects.filter(email_pre_autorizzata=data['email']).exists():
            raise serializers.ValidationError({'email': 'Questa email non risulta tra i partecipanti autorizzati.'})

        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        # Creiamo l'utente. Stiamo collegando l'utente al profilo partecipante esistente
        user = User.objects.create_user(**validated_data, is_participant=True)
        partecipante = Partecipante.objects.get(email_pre_autorizzata=user.email)
        partecipante.user = user
        partecipante.save()

        return user
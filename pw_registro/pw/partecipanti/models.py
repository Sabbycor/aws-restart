from django.db import models
import uuid
from django.conf import settings
from django.db import models


class Partecipante(models.Model):
    #riferimento a user con fk
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="participant_profile"
    )

    data_iscrizione = models.DateField(null=True, blank= True)
    
    
    
    
class Meta:
    db_table = "partecipanti"
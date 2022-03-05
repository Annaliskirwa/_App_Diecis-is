from rest_framework import serializers 
from tutorialsnow.models import Tutorial

class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
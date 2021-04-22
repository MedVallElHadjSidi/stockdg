from rest_framework import serializers 
from stockColi.models import Client
from stockColi.models import Depot
from stockColi.models import Envoi
 



class EnvoiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Envoi
		fields = (
			'reference',
			'capaciter',
			'typeEnvoi',
			'lieuDepart',
			'lieuArriver',
			'status',
			'dateDepart',
			'dateArriver'
			)
 
class ClientSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Client
        fields = ('numeroClient',
                  'nomClient',
                  'email',
                  'numeroTel',
                  'numeroWhatsapp')


class DepotSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Depot
        fields = ('nomDepot',
        	      'adresse',
        	      'lieu',
                  'statusDp'
                  )
from django.shortcuts import render
from rest_framework.views import APIView, Response

from .models import Pokemon

from move_app.models import Move

from django.core.serializers import serialize

import json


# Create your views here.
class All_pokemon(APIView):
    def get(self,request):
        pokemon = Pokemon.objects.order_by('name')
        serialized_pokemon = serialize('json',pokemon)
        json_pokemon = json.loads(serialized_pokemon)
        
        for pokemon in json_pokemon:
            move_data = Move.objects.filter(id__in=pokemon['fields']['moves'])
            pokemon['fields']['moves'] = json.loads(serialize('json',move_data))
        return Response(json_pokemon)
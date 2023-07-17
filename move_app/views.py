from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView, Response
# We want to bring in our model
from .models import Move
# serialize will turn querysets into binary string
from django.core.serializers import serialize
# Json will turn binary string into JSON readable data
import json

# Create your views here.
class All_moves(APIView):
    # specify which request method should trigger this behavior
    def get(self, request):
        # grab a binary string of all Moves in the DB ordered by name
        moves = serialize('json', Move.objects.all().order_by('name'))
        # utilize json.loads to turn moves into JSON Data
        moves = json.loads(moves)
        return Response(moves)
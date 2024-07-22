from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Talents
from .serializers import TalentSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        "GET /api",
        "GET /api/talents",
        "GET /api/talents/:id",
    ]
    return Response(routes)


@api_view(['GET'])
def get_talents(request):
    talents = Talents.objects.all()
    serializer = TalentSerializer(talents, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_talent(request, id):
    talent = Talents.objects.get(id=id)
    serializer = TalentSerializer(talent, many=False)
    return Response(serializer.data)

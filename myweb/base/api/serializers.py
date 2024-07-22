from rest_framework.serializers import ModelSerializer
from ..models import Talents


class TalentSerializer(ModelSerializer):
    class Meta:
        model = Talents
        fields = '__all__'

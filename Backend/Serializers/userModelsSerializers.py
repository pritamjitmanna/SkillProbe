from rest_framework import serializers
from ..Models.userModel import Candidate,Company


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model=Candidate
        fields='__all__'

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model=Company
        fields='__all__'
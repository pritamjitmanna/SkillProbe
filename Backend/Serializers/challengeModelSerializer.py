from ..Models.challengeModels import Challenge,TestCase,Coding,MCQ
from rest_framework import serializers


class ChallengeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Challenge
        fields='__all__'


class TestCaseSerializer(serializers.ModelSerializer):

    class Meta:
        model=TestCase
        fields='__all__'


class CodingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Coding
        fields='__all__'


class MCQSerializer(serializers.ModelSerializer):

    class Meta:
        model=MCQ
        fields='__all__'




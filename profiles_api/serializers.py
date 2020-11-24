from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
	"""Serializes a name for testing our APIView"""
	"""serializers also take care of field validation"""
	"""make serializer for post request"""
	name=serializers.CharField(max_length=10)

#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from profiles_api import serializers #gonna use to tell api view what data to expect whene making post and patch requests


# Create your views here.
class HelloApiView(APIView):
	"""Test API View. creates a new class based on API view class Django provides
	and allows us to define an application logic for our endpoint(URL) that we are
	going to assign to this view. You define a URL(endpoint) and assign to the view
	and Django rest framework handles it by calling the appropriate function
	in the view for the HTTP request that you make.
	APIView expects a function for the different HTTP requests that can 
	be made to the view"""
	'we are going to be an accepting an HTTP get request to our API'
	'get is usually used to request list of objects'
	'so when you make an HTTP get request to the URL assigned to the apiview, it would call the get function and execute the logic in that get function'
	serializer_class = serializers.HelloSerializer #would put a name field on page
	def get(self, request, format=None):
		"""Returns a list of APIView features"""
		"""request is passed in by rest framework and contains details of the request being made to the API"""
		"""get, post, etc are functions you can add to api view
		to support the different HTTP requests"""
		an_apiview=[
			'Uses HTTP methods as function[get, post, patch, put, delete',
			'is similar to a traditional Django view',
			'gives you the most control over your application logic',
			'is mapped manually to URLs', ]
		"""every function must return a response object"""
		"""response needs to contain a dictionary or list which it would then output when api called
		converts response json. To convert response obj to json, needs a list or dict"""
		return Response({'message': 'Hello', 'an_apiview': an_apiview})

	def post(self, request):
		"""Create a hello message with our name"""
		"""self.serializer is standard way to retrieve a serializer class when working in view"""
		"""assigning data:when making post requeests, data gets passed in as request.data"""
		"""request.data is assigned to serializer_class in new var serializer"""
		serializer=self.serializer_class(data=request.data)

		if serializer.is_valid():
			name=serializer.validated_data.get('name')
			message=f'Hello {name}'
			return Response({'message':message})
		else:
			return Response(
				serializer.errors, 
				status=status.HTTP_400_BAD_REQUEST
				)

	def put(self, request, pk=None):
		#pk is usually primary key of object
		"""Handle updating an object"""
		return Response({'method':'PUT'})

	def patch(self, request, pk=None):
		"""Patch an object"""
		return Response({'method':'PATCH'})

	def delete(self, request, pk=None):
		"""Delete an object"""
		return Response({'method': 'DELETE'})

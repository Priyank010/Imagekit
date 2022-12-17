from rest_framework import viewsets
from .models import *
from .serializers import *
from imagekitio import ImageKit
from rest_framework.views import APIView
from .tests import *
from rest_framework.response import Response

class PhotographersViewSet(viewsets.ModelViewSet):
    serializer_class = PhotographersSerializer
    queryset = Photographers.objects.all()

class ImagekitAuth(APIView):

	def get(self, request):
	
		imagekit = ImageKit(
		public_key='public_0MJDu5MtdCz17CdEuntDFiCehAQ=',
		private_key='private_dCvrS1uHXO7iepoq8Z/MDVv7ENo=',
		url_endpoint = 'https://ik.imagekit.io/nmwe3y5at')

		auth_params = imagekit.get_authentication_parameters()

		token = list(auth_params.values())[0]
		expire = list(auth_params.values())[1]
		signature = list(auth_params.values())[2]

		data_obj = imagekitAuthTest(token,expire,signature)
		serializer_class = ImagekitAuthSerializer(data_obj)
		return Response(serializer_class.data)
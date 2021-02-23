from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.shortcuts import redirect, render
from rest_framework import generics, viewsets, status
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, \
    HTMLFormRenderer, AdminRenderer, TemplateHTMLRenderer, MultiPartRenderer
from rest_framework.views import APIView
from ..ipstack_API import get_coordinates
from ..models import Geolocation
from .serializers import GeolocationSerializer
from rest_framework.response import Response


class GeolocationListCreate(APIView):
    """
    List geolocations based on IP, or savea actual geolocation to DB.
    """
    serializer_class = GeolocationSerializer

    def get(self, request, format=None):
        geolocation = Geolocation.objects.filter(user_name=request.user.id)
        serializer = GeolocationSerializer(geolocation, many=True)
        # print('-' * 10, '>', type(serializer.data))
        # print('-' * 10, '>', list(serializer.data))
        return Response(serializer.data)

    def post(self, request, format=None):
        api_request_data = get_coordinates()
        api_request_data['user_name'] = request.user.pk
        serializer = GeolocationSerializer(data=api_request_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(user_name=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeolocationActual(APIView):
    """
    Shows actual geolocation.
    """
    def get(self, request):
        return Response(get_coordinates())


class GeolocationDelete(APIView):
    """
    Shows detail of geolocation and delete it.
    """
    def get_object(self, request, pk):
        try:
            return Geolocation.objects.filter(
                user_name=request.user.id).get(pk=pk)
        except Geolocation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        geolocation = self.get_object(request, pk)
        serializer = GeolocationSerializer(geolocation)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        geolocation = self.get_object(request, pk)
        geolocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


################################
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('geolocation_list_create')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

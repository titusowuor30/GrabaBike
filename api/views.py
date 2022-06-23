from http import client
from django.contrib.auth import authenticate
from api.serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .models import *
from django.contrib.auth import logout
from .serializers import *
import json
from json import JSONEncoder


class UserCreate(generics.CreateAPIView):
    permission_classes = ()
    serializer_class = UserSerializer

    # def perform_create(self, serializer):
    #     team = User.objects.filter(members__in=[self.request.user]).first()

    #     serializer.save(team=team, created_by=self.request.user)

    # def get_queryset(self):
    #     team = User.objects.filter(members__in=[self.request.user]).first()

    #     return self.queryset.filter(team=team)


class LogOutView(APIView):
    permission_classes = ()

    def post(self, request,):
        logout(request.user)
        return Response({"Logout Success!"}, status=status.HTTP_200_OK)


class LoginView(APIView):

    permission_classes = ()
    serializer_class = UserSerializer

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"user": {"username": user.username, "email": user.email, "id": user.id, "token": user.auth_token.key}, "roles": user.roles.values()})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.TokenAuthentication,)


class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer


class RiderCreate(generics.CreateAPIView):
    # queryset = ParkingInfo.objects.create()
    serializer_class = RiderSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.TokenAuthentication,)


class RidesViewSet(viewsets.ModelViewSet):
    queryset = Rides.objects.all()
    serializer_class = RidesSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.TokenAuthentication,)


class RideCreate(generics.CreateAPIView):
    # queryset = ParkingInfo.objects.create()
    serializer_class = RidesSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.TokenAuthentication,)


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (authentication.TokenAuthentication,)


class TransactionsCreate(generics.CreateAPIView):
    # queryset = ParkingInfo.objects.create()
    serializer_class = TransactionsSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (authentication.TokenAuthentication,)


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (authentication.TokenAuthentication,)


class RolesCreate(generics.CreateAPIView):
    # queryset = ParkingInfo.objects.create()
    serializer_class = TransactionsSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.TokenAuthentication,)


@api_view(['GET', 'POST'])
# @authentication_classes()
@permission_classes([])
def confirm_rides(request):
    if request.method == 'POST':
        print(request.data)
        print(request.data['riderid'])
        print(request.data['client'])
        client = request.data['client']
        rider = request.data['riderid']
        command = request.data['command']
        print(command)
        if command == 'accept':
            rides = Rides.objects.get(client__username=client, rider=rider)
            rides.confirmed = True
            rides.save()
            print(rides)
            return Response({"Ride confirmed successfully!"})
        else:
            rides = Rides.objects.get(client__username=client, rider=rider)
            rides.confirmed = False
            rides.save()
            print(rides)
            return Response({"Ride cancelled successfully!"})


@api_view(['GET', 'POST'])
# @authentication_classes()
@permission_classes([])
def complete_rides(request):
    if request.method == 'POST':
        try:
            rideid = request.data['rideid']
            rider = request.data['rider']
            client = request.data['client']
            paymethod = request.data['paymethod']
            amount = request.data['amount']
            trcode = request.data['trcode']
            rating = request.data['rating']
            comments = request.data['comments']
            rides = Rides.objects.get(id=rideid)
            rides.completed = True
            rides.rating = int(rating)
            rides.comments = comments
            rides.save()
            print(rides)
            transactions = Transactions.objects.create(
                transaction_code=trcode,
                pyment_method=paymethod,
                amount=float(amount),
                rideid=rideid
            )
            transactions.save()
            print(transactions)
        except Exception as e:
            return Response({"Error:"+str(e)})
    return Response({"Ride completed successfully!\nThank you for choosing us!"})

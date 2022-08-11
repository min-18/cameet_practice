
from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class UserList(APIView):
    
    # 역참조를 통해 user가 생성한 방을 보고싶다!
    def get(self, request):

        users = User.objects.all()
        # rooms = Room.objects.all()
        # print(dir(users))
        # 많은 유저 받아오려면 (many=True) 써줘야 한다! 이렇게 에러뜨는 경우가 생각보다 많다...
        serializer = UserSerializer(users, many=True)

        # serializer2 = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        # db에 담기 위해 디시리얼라이즈?
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RoomList(APIView):

    def get(self, request):
        
        room = Room.objects.all()
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)

class RoomDetailAPIView(APIView):
    
    def get_object(self, pk):
        room = get_object_or_404(Room, pk=pk)
        # room_info = room.user__id
        return room
    
    def get(self, request, pk):
        # 특정 pk값에 해당하는 room 객체 가져옴.
        room = self.get_object(pk)
        serializer = RoomSerializer(room)
        print(serializer)
        return Response(serializer.data)


from dataclasses import field, fields
from rest_framework import serializers
from .models import *

# 정참조로 하고 뷰에서 역참조조작


class UserSerializer(serializers.ModelSerializer):

    # 유저가 생성한 방들 가져오기 위해 역참조

    # 역참조 ; 여기 변수는 FK부분 related_name 이랑 같아야함.
    # rooms = RoomSerializer(many=True, read_only=True)
    # rooms = serializers.StringRelatedField(many=True)

    user_create_rooms = serializers.SerializerMethodField()

    class Meta:
        model = User
        # fields = '__all__'      # 필요한 필드만 하고 싶을 땐 리스트 형태로 작성. ; fields = ['id', 'title']
        # User객체에 없는, room정보도 SerializerMethodField()로 가져온 변수도 넣어주기!
        fields = ('name', 'age', 'created', 'user_create_rooms')

    # get_(변수명)이어야 올바르게 작동한다.
    def get_user_create_rooms(self, obj):

        room_list = []

        for room in obj.rooms.all():
            print(room)
            room_json = {
                'room_id': room.id,
                'room_title' : room.room_title,
                'room_interest' : room.room_interest,
            }

            room_list.append(room_json)

        print(room_list)
        # 문제) 지금 room_list 는 json으로 시리얼라이즈 되지 않았다,,, ->객체들을 json 형태로 하나씩 담아주는 방법 선택

        return room_list



# 룸정보 안에 유저정보까지
class RoomSerializer(serializers.ModelSerializer):

    # user_id = serializers.StringRelatedField()
    
    # 중요) 변수명을 모델에서 쓴 변수명으로 통일해줘야 함.(FK필드)
    # 참고로 방의 호스트(user)는 한명이니 many=True 써주면 안된다.
    user_key = UserSerializer()
    print(user_key)

    # user_key = UserSerializer(read_only = True)    

    class Meta:
        model = Room
        # fields = [ 'room_title', 'user']
        fields = '__all__'
        # fields = ['id', 'user_key', 'room_title', 'room_interest']
        # unique_together = ['user_id', 'room_title']







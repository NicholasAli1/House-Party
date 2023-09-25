from django.urls import path
from api.views import RoomView, CreateRoomView, GetRoom

urlpatterns = [
    path("room", RoomView.as_view(), name="room-create"),
    path("create-room", CreateRoomView.as_view(), name="create-room"),
    path("get-room", RoomView.as_view(), name="get-room"),
]

from django.urls import path
from api.views import RoomView

urlpatterns = [
    path("room", RoomView.as_view(), name="room-create"),  
]

from django.urls import path

from board.views import board

urlpatterns = [
    path('', board)
]
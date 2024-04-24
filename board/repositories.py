
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response

from board.models import Board
from board.serializers import BoardSerializer
import pytz
from django.shortcuts import get_object_or_404


class BoardRepository(object):

    def __init__(self):
        pass

    def get_all(self):
        return Response(BoardSerializer(Board.objects.all(), many=True).data)

    def user_board(self, req):
        return Response(BoardSerializer(Board.objects.all().filter(author=req['author'])))

    def update_board(self, req):
        board = get_object_or_404(Board, custom_id=req['customId'])
        board.title = req['title']
        board.content = req['content']
        board.save()
        updated_board = Board.objects.filter(custom_id=req['customId'])
        return BoardSerializer(updated_board, many=True).data

    def delete_board(self, custom_id):
        board = get_object_or_404(Board, custom_id=custom_id)
        board.delete()
        return True

    def find_board_exists(self, id):
        return Board.objects.all().filter(id=id).exists()

    def get_board(self):
        user_board = Board.objects.all().values()
        user_board_ls = [
            {
                **board,
                'time': board['time'].astimezone(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S'),
                'modification_time': board['modification_time'].astimezone(pytz.timezone('Asia/Seoul')).strftime(
                    '%Y-%m-%d %H:%M:%S')
            } for board in user_board
        ]
        print(user_board_ls)
        return user_board_ls


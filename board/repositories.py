
from rest_framework.response import Response

from board.models import Board
from board.serializers import BoardSerializer
from django.core.paginator import Paginator
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
        return Board.objects.all().filter(custom_id=id).exists()

    def find_board_for_id(self, id):
        try:
            user_board = Board.objects.get(custom_id=id)

            formatted_board = {
                'custom_id': user_board.custom_id,
                'title': user_board.title,
                'content': user_board.content,
                'time': user_board.time.astimezone(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S'),
                'modification_time': user_board.modification_time.astimezone(pytz.timezone('Asia/Seoul')).strftime(
                    '%Y-%m-%d %H:%M:%S'),
                'author': {
                    'id': user_board.author.id,
                    'nickname': user_board.author.nickname
                }
            }
        except Board.DoesNotExist:
            return {'error': 'No Board found with the given custom_id'}

        return formatted_board

    def get_page_board(self, page):
        per_page = 10

        # 최신 순서로 정렬
        user_board = Board.objects.all().select_related('author').order_by('-time')

        # 페이지네이션 설정
        paginator = Paginator(user_board, per_page)
        page_obj = paginator.get_page(page)

        # 데이터 포맷 변경
        user_board_ls = [
            {
                'custom_id': board.custom_id,
                'title': board.title,
                'content': board.content,
                'time': board.time.astimezone(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S'),
                'modification_time': board.modification_time.astimezone(pytz.timezone('Asia/Seoul')).strftime(
                    '%Y-%m-%d %H:%M:%S'),
                'author_id': board.author.id,
                'author_nickname': board.author.nickname
            } for board in page_obj
        ]

        response_data = {
            'total_count': paginator.count,
            'total_pages': paginator.num_pages,
            'current_page': page,
            'data': user_board_ls
        }
        return response_data


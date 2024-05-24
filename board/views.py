from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from board.repositories import BoardRepository
from board.serializers import BoardSerializer


# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def board(request):
    print(f"data : {request.data}")
    if request.method == "POST":
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print('게시물 저장')
            return JsonResponse({'data' : '작성이 완료 되었습니다!'}, safe=False)
        else:
            print('게시물 저장중 에러')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        if 'customId' in request.GET:
            customId = request.GET['customId']
            return JsonResponse(BoardRepository().find_board_for_id(customId), safe=False)
        else:
            page = request.GET['page']
            return JsonResponse(BoardRepository().get_page_board(page), safe=False)
    elif request.method == "PUT":
        updated_data = BoardRepository().update_board(request.data)
        return Response(updated_data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        print(request.GET['customId'])
        success = BoardRepository().delete_board(request.GET['customId'])
        if success:
            return HttpResponse(status=204)
        else:
            return JsonResponse({'error': '해당 게시물을 찾을 수 없습니다.'}, status=404)




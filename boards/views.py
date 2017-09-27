from django.http import HttpResponse
from boards.models import Board


def home(request):
    boards = Board.objects.all()
    boards_names = [board.name for board in boards]
    html_response = '<br>'.join(boards_names)
    return HttpResponse(html_response)

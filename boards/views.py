from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from boards.models import Board
from .models import Board, Topic, Post


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    """New topic view

    Renders and returns the new topic view based on the input request
    :param request: http request
    :type request: get
    :param pk: primary key for the boards model
    :type pk: int
    :returns: rendered response
    :rtype: {render}
    """
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        # TODO get currently logged in user
        user = User.objects.first()

        topic = Topic.objects.create(subject=subject,
                                     board=board,
                                     starter=user)
        Post.objects.create(message=message, topic=topic,
                            created_by=user)

        # TODO redirect them to the newly created topics page
        return redirect('board_topics', pk=board.pk)

    return render(request, 'new_topic.html', {'board': board})

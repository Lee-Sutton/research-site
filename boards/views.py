"""Views for the forms application"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from boards.forms import NewTopicForm
from boards.models import Board, Post


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
    user = User.objects.first()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            Post.objects.create(message=form.cleaned_data.get('message'),
                                topic=topic,
                                created_by=user)
            return redirect('board_topics', pk=board.pk)

    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})

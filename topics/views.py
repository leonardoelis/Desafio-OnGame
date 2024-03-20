from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Topic, Comment
from .forms import TopicForm, CommentForm


def index(request):
    topics = Topic.objects.all()
    context = {}
    context['topics'] = topics
    return render(request, 'topics/index.html', context)


def register_topic(request):
    if request.user.is_anonymous:
        return redirect('login')

    context = {}
    if request.method == 'POST':
        if request.FILES:
            form = TopicForm(request.POST, request.FILES)
        else:
            form = TopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('show_topic', id=topic.id)
    else:
        form = TopicForm()

    context['form'] = form
    return render(request, 'topics/registerTopic.html', context)


def show_topic(request, id):
    topic = Topic.objects.get(id=id)
    comments = Comment.objects.filter(topic=id)

    form = CommentForm()
    context = {}
    context['topic'] = topic
    context['comments'] = comments
    context['form'] = form
    return render(request, 'topics/showTopic.html', context)


@require_POST
def register_comment(request, id):
    if request.user.is_anonymous:
        return redirect('login')

    topic = Topic.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.author = request.user
            comment.save()
            return redirect('show_topic', id=id)



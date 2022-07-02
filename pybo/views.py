from django.shortcuts import render
from django.http import HttpResponse
from pybo.models import Question
# Create your views here.

def index(request):
    #질문먹록 출력
    q=Question.objects.order_by('-create_date')
    context = {'question_list': q}
    return render(request, 'pybo/question_list.html', context)
    
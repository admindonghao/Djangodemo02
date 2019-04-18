from django.shortcuts import render
from django.http import HttpResponse
from .models import IssueList, ChioceList


# Create your views here.
def index(request):
    return render(request, 'polls/index.html', {})


def list(request):
    pl = IssueList.objects.all()
    return render(request, 'polls/list.html', {'polls':pl})


def detail(request, id):
    poll = IssueList.objects.get(pk=id)
    return render(request, 'polls/detail.html', {'poll':poll})


def details(request, id):
    poll = IssueList.objects.get(pk=id)
    po = request.POST['poll']
    # print(po)
    cho = ChioceList.objects.get(pk=po)
    # print(cho)
    cho.number += 1
    cho.save()
    return render(request, 'polls/details.html', {'poll':poll})
    # return HttpResponse('h1')
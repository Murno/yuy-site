from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# Create your views here.


def index(request):

    list_members = Member.objects.all()

    print(list_members)

    context = {
        'list_members' : list_members
    }

    return render(request, 'index.html', context)


def member(request, id):

    get_member = Member.objects.get(id=id)

    context = {
        'member' : get_member,
    }

    return render(request, 'member.html', context)

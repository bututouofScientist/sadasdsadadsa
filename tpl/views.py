from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader


def index(request):
    messages.debug(request, '这是一条message信息')
    return render(request, 'tpl_index.html')


def find(request):
    template = loader.get_template('tpl_index.html')
    content = template.render(context={'content': 'hello world'}, request=request)
    print(content)
    return HttpResponse(content)

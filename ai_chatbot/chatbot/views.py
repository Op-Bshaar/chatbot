from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def chatbot(request):
     template = loader.get_template('chatbot.html')
     return HttpResponse(template.render({},request))
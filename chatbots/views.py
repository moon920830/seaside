from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def chatbots(request):
  template = loader.get_template('chatbots.html')
  return HttpResponse(template.render())

def chat_bot(request):
  template = loader.get_template('chat_bot.html')
  return HttpResponse(template.render())

def motor_bot(request):
  template = loader.get_template('motor_bot.html')
  return HttpResponse(template.render())

def health_bot(request):
  template = loader.get_template('health_bot.html')
  return HttpResponse(template.render())

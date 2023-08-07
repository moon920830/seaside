from django.http import HttpResponse
from django.template import loader

def services(request):
  template = loader.get_template('services.html')
  return HttpResponse(template.render())

def bot_listing(request):
  template = loader.get_template('bot_listing.html')
  return HttpResponse(template.render())

def ml(request):
  template = loader.get_template('ml.html')
  return HttpResponse(template.render())

def custom_apps(request):
  template = loader.get_template('custom_apps.html')
  return HttpResponse(template.render())

def auto_cloud(request):
  template = loader.get_template('auto_cloud.html')
  return HttpResponse(template.render())

def commerce(request):
  template = loader.get_template('commerce.html')
  return HttpResponse(template.render())

def market_automation(request):
  template = loader.get_template('market_automation.html')
  return HttpResponse(template.render())


from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
  return HttpResponse("<h1>Index Page</h1>")

def hello(request, username):
  return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
  return HttpResponse("<h1>About this app</h1>")




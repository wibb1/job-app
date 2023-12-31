from xmlrpc.server import list_public_methods
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template import loader

from app import urls
from app.models import JobPost

job_title = [
  "First Job", "Second Job", "Third Job", 
]

job_description = [
  "First Job Description", "Second Job Description", "Third Job Description"
]

def job_list(request):
  jobs = JobPost.objects.all()
  context = {
    'jobs': jobs
  }
  return render(request, 'app/job_list.html', context)

def job_detail(request, id):
  try:
    if(id == 0):
      return redirect(reverse('job_home'))
    context = {
      'job': JobPost.objects.get(id=id)
    }
    
    return render(request, 'app/job_detail.html', context)
  except Exception:
    return HttpResponseNotFound("Not Found")

def hello(request):
  context = {
    'name':'Samwise',
    'first_list': ["alpha", "beta"],
    'temp_object': TempClass(),
    'age': 53,
    'is_authenticated': True,
  }
  return render(request, 'app/hello.html', context)

class TempClass:
  x = 5
  
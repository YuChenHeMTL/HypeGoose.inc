from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
# Create your views here.

import os 

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.files.storage import default_storage


def file_upload(request):
    save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
    path = default_storage.save(save_path, request.FILES['file'])
    return default_storage.path(path)


from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from PhotoAlbum.models import Albumb2017
from django.conf import settings
import os
import requests
import subprocess
import threading
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
import atexit
import socket
import time
import psutil

# Create your views here.

OPENWEBUI_PORT = 8080

def is_openwebui_running():
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            if proc.name() == 'open-webui' or \
                (proc.cmdline() and 'open-webui' in proc.cmdline()[0]):
                return True
        except:
            continue
    return False

@csrf_exempt
def openwebui_proxy(request):
    response = requests.request(
        method=request.method,
        url=f"http://localhost:8080{request.path}",
        headers = {k:v for k,v in request.headers.items() if k.lower() != 'host'},
        data=request.body,
        params=request.GET,
        stream=True
    )

    proxy_response = StreamingHttpResponse(
        streaming_content=response.iter_content(chunk_size=8192),
        content_type=response.headers.get('Content-Type'),
        status=response.status_code
    )

    for k, v in response.headers.items():
        if k.lower() in ['content-type', 'content-length']:
            proxy_response[k] = v

    return proxy_response

def openwebui_embed(request):
    if is_openwebui_running():
        return render(request, 'openwebui_embed.html', {
            'openwebui_path': f'http://localhost:{OPENWEBUI_PORT}'
        })
    else:
        return render(request, 'wrong.html')

def wrong(request):
    return render(request, 'wrong.html')

def home(request):
    return render(request, 'home.html')


def album2017(request):
    img_list = Albumb2017.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(img_list, 50)
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)

    return render(request, 'album2017.html', {"images": images})


def mml(request):
    global img_path
    img_list =Albumb2017.objects.all()
    if request.method == "GET":
        return render(request, "ManageMediaLibrary.html", {"img_list": img_list})
    path = request.POST.get("path")
    print(path)
    path1 = path.split('/')
    sub_path = os.listdir(path)
    print(sub_path)
    for i in range(len(sub_path)):
        sub_path2 = os.listdir(os.path.join(path, sub_path[i]))
        for j in range(len(sub_path2)):
            print(sub_path2[j])
            Albumb2017.objects.create(img_path=os.path.join("/static/media/",path1[-1], sub_path[i], sub_path2[j]), pic_time=sub_path[i])

    img_list = Albumb2017.objects.all()
    return render(request, "ManageMediaLibrary.html", {"Album": img_list})

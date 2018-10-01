from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .recognizer import recognizer
from .img_utils import dataurl_to_pil
import tensorflow as tf

def index(request):
    template = loader.get_template('handwritten_digits/index.html')
    context = {
        'header': 'Write one digit in the black canvas',
        'draw': True,
    }
    return HttpResponse(template.render(context, request))

def recognize(request):
    # get the dataURL of the image
    # todo: make it possible in mobile devices (mouse event not supported)
    template = loader.get_template('handwritten_digits/index.html')
    # TODO: change the path to some better practi
    data = request.POST['dataURL'].split(',')[1]
    image = dataurl_to_pil(data)
    context = {
        'header': 'Recognize result',
        'result': recognizer.recognize(image),
        'dataURL': 'data:image/png;base64,' + data
    }
    return HttpResponse(template.render(context, request))
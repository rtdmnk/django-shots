from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import glob
import re

# Create your views here.
def index(request):
    imagepath = settings.BASE_DIR + "/media/screens/thumbs/"
    _images = glob.glob(imagepath + "*.png")

    images = []
    for image in _images:
        image = image.replace(imagepath, "")
        images.append(image)

    images.sort()
    content = {'images': images}
    return render(request, 'shots/index.html', content)

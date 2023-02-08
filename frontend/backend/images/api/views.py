from rest_framework import viewsets
from .serializers import ImageSerializer
from ..models import Image
from rest_framework.decorators import action
from django.http import HttpResponse
from wsgiref.util import FileWrapper

class ImageViewSets(viewsets.ModelViewSet):
    queryset=Image.objects.all()
    serializer_class=ImageSerializer
    #/api/images/ -> to view all images
    #/api/images/<pk>/ -> to view particular image
    #/api/images/<pk>/download -> to download a particular image

    @action(methods=['GET'], detail=True)
    #def download(self, request, pk):
    def download(self, *args, **kwargs):
        instance=self.get_object()
        pic_path=instance.rmbg_pic.path
        pic=open(pic_path, 'rb')
        response=HttpResponse(FileWrapper(pic), content_type="image/png")
        return response
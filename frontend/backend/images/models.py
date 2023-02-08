from django.db import models
import PIL
import numpy as np
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from io import BytesIO
import os
from django.core.files.base import ContentFile
# Create your models here.
class Image(models.Model):
    pic=models.ImageField(upload_to="images")
    rmbg_pic=models.ImageField(upload_to="images_rmbg", blank=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        pil_pic=PIL.Image.open(self.pic)
        pic=np.array(pil_pic)
        segmentor=SelfiSegmentation()
        rmbg=segmentor.removeBG(pic, (0, 255, 0), threshold=0.4)
        buffer=BytesIO()
        output_pic=PIL.Image.fromarray(rmbg)
        output_pic.save(buffer, format="png")
        val=buffer.getvalue()
        filename=os.path.basename(self.pic.name)
        name, extension = filename.split(".")
        self.rmbg_pic.save(f"bgrm_{name}.png", ContentFile(val), save=False)
        super().save(*args, **kwargs)


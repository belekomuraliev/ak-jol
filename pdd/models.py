from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

from ak_jol_user.models import Author


def compress_image(img, file_format='webp', new_width=None, new_height=None ):
    image = Image.open(img)
    width, height = image.size
    if new_width and new_height:
        image = image.resize((new_width, new_height))
    elif new_width:
        new_height = int(new_width / width * height)
        image = image.resize((new_width, new_height))
    elif new_height:
        new_width = int(new_height / height * width)
        image = image.resize((new_width, new_height))
    image_io = BytesIO()
    image.save(image_io, format=file_format, optimize=True)
    new_image = File(image_io, name=f"{img.name.split('.')[0]}.{file_format}")
    return new_image


class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name='Вопрос')
    image = models.ImageField(upload_to="photos", blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.image = compress_image(self.image, new_width=600)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=255, blank=True)
    answer = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)





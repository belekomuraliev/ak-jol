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
    questionNamber = models.IntegerField(unique=True, auto_created=True)
    text = models.CharField(max_length=255, verbose_name='Вопрос')
    image = models.ImageField(upload_to="photos", blank=True)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.image = compress_image(self.image, new_width=500)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.questionNamber} - {self.text}'


class Answer(models.Model):
    text = models.CharField(max_length=255, blank=True, null=True)
    answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.questionNamber} - {str(self.text)}'


class Blog(models.Model):
    blogNamber = models.IntegerField(unique=True, auto_created=True, blank=True, null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    blog_image = models.ImageField(upload_to="photos/blog", blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.blog_image = compress_image(self.blog_image, new_width=400)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.blogNamber} - {self.title}'

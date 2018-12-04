from django.db import models
from django.utils import timezone

from tinymce.models import HTMLField

# Create your models here.


def true_xor(*args):
    return sum(args) == 1


class Project(models.Model):
    background = models.ImageField(upload_to="backgrounds/")
    title = models.CharField(max_length=100)
    presentation_text = models.TextField(null=True)
    date_project = models.DateField()

    date_upload = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=True)
    view_order = models.IntegerField(choices=(
        (1, 'top left'),
        (2, 'top right'),
        (3, 'bottom left'),
        (4, 'bottom right'),),
        null=True, blank=True, unique=True)

    image = models.ImageField(upload_to="images/", blank=True)
    video = models.FileField(upload_to="videos/", blank=True)
    text = HTMLField(blank=True)

    class Meta:
        verbose_name = "projet"

    def clean(self):
        if not self.is_visible:
            self.view_order = None

    def __str__(self):

        return f"{self.title} - {self.date_project.year}"

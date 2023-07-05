from django.db import models
from django.urls import reverse


class Sets(models.Model):
    set_name = models.CharField(max_length=255, db_index=True)
    bonus = models.TextField()

    def get_absolute_url(self):
        return reverse('set', kwargs={'set_id': self.pk})

    def __str__(self):
        return self.set_name

    class Meta:
        verbose_name = 'Комплекты'
        verbose_name_plural = 'Комплекты'


class Artifacts(models.Model):
    title = models.CharField(max_length=255)
    stats = models.TextField()
    price = models.IntegerField()
    history = models.TextField()
    slot = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    set = models.ForeignKey(Sets, on_delete=models.DO_NOTHING)
    time_create = models.DateTimeField(auto_now_add=True, blank=True)
    time_update = models.DateTimeField(auto_now=True, blank=True)
    is_published = models.BooleanField(default=True, blank=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Артефакты'
        verbose_name_plural = 'Артефакты'

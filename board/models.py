from django.db import models


from kakao.models import Kakao


# Create your models here.


class Board(models.Model):
    custom_id = models.AutoField(primary_key=True, unique=True)
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(Kakao, on_delete=models.CASCADE)

    class Meta:
        db_table = 'board'

    def __str__(self):
        return f'{self.pk}'

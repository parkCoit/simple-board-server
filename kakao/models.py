from django.db import models

# Create your models here.


class Kakao(models.Model):
    id = models.CharField(primary_key=True, max_length=50, unique=True)
    nickname = models.TextField(max_length=100)

    class Meta:
        db_table = 'kakao'

    def __str__(self):
        return f'{self.pk} {self.nickname}'


class KakaoToken(models.Model):
    token = models.CharField(primary_key=True, max_length=255, unique=True)

    id = models.ForeignKey(Kakao, on_delete=models.CASCADE)

    class Meta:
        db_table = 'kakao_token'

    def __str__(self):
        return f'{self.pk} {self.id}'


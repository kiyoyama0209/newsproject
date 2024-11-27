from django.db import models
from accounts.models import CustomUser
class Category(models.Model):
    title = models.CharField(verbose_name = 'カテゴリ',max_length = 20,null=True,blank=True)
    
    def __str__(self):
        return self.title

class ArticlePost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )
    content = models.TextField(
        verbose_name='記事内容'
    )
    image = models.ImageField(
        verbose_name= 'イメージ',
        upload_to = 'photos'
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add = True
    )
    def __str__(self):
        return self.title
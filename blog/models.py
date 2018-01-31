from django.contrib.auth.models import User
from django.db import models
from django.urls import  reverse
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100) # 分类名称

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100) # 标签

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70) # 文章标题
    body = models.TextField() # 文章内容
    created_time = models.DateTimeField() # 创建时间
    modified_time = models.DateTimeField() # 最后一次修改时间
    excerpt = models.CharField(max_length=200, blank=True) # 文章摘要
    category = models.ForeignKey(Category) # 绑定分类
    tags = models.ManyToManyField(Tag, blank=True) # 绑定标签
    author = models.ForeignKey(User) # 作者

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        obj = reverse('blog:detail', kwargs={'pk':self.pk})
        return obj


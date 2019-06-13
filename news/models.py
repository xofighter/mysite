from django.db import models

# Create your models here.
'''
设计模型
Django 无需数据库就可以使用，它提供了`对象关系映射器`通过此技术，你可以使用`Python`代码来描述数据库结构。
你可以使用强大的`数据-模型语句`来描述你的数据模型，这解决了数年以来在数据库模式中的难题。以下是一个简明的例子：
'''
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
from django.db import models

# Create your models here.

# 文章模型的定义
class Article(models.Model):
    # 文章的唯一ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章主要内容
    content = models.TextField()
    # 文章的发布日期
    publish_date = models.DateTimeField(auto_now=True)

    # 返回文章title
    def __str__(self):
        return self.title
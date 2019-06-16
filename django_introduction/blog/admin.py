from django.contrib import admin

# Register your models here.
from  .models import Article
# 将Article模型（类）引进来

admin.site.register(Article)
# 将Aractle模型注册到admin模块中

from django.urls import path,include
# 引进django路由配置相关的包
import blog.views
# 引入视图文件

# 路由配置
urlpatterns = [
    path('hello_world',blog.views.hello_world),
    # 如果URL中含有hello_world就转发到blog.views.hello_world视图函数中
    path('content',blog.views.article_content),
    # 如果URL中含有content就转发到blog.views.article_content视图函数中
    path('index',blog.views.get_index_page),
    # path('detail',blog.views.get_detail_page)
    path('detail/<int:article_id>',blog.views.get_detail_page)
    # 通过article_id实现文章详情页面的跳转
]

from django.shortcuts import render
from django.http import HttpResponse
# 引进HttpResponse
# Create your views here.
from blog.models import Article
# 引入models中Article类

from django.core.paginator import Paginator
# 引入django分页组件

# 定义一个函数接受request请求，返回字符串hello world！
def hello_world(request):
    # 返回HttpResponse
    return HttpResponse('hello world！')

# 定义一个函数接受request请求，返回第一篇博客文章数据
def article_content(request):
    article = Article.objects.all()[0]
    # all返回的是QuerySet对象，程序并没有真的在数据库中执行SQL语句查询数据，但支持迭代，使用for循环可以获取数据。
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title:{},brief_content:{},content:{},article_id:{},' \
                 'publish_date:{}'.format(title,brief_content,content,article_id,publish_date)
    return HttpResponse(return_str)

# 定义一个函数，接受request参数
def get_index_page(request):
    page = request.GET.get('page')
    # 获取请求中传递过来的page参数
    if page:
        page = int(page)
    else:
        page = 1
    print('page param:',page)
    all_article =  Article.objects.all()
    # 取出所有文章
    top4_article_list = Article.objects.order_by('-publish_date')[:4]
    paginator = Paginator(all_article,4)
    page_num = paginator.num_pages
    print('page num',page_num)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request,'blog/index.html',{
        'article_list':page_article_list,
        'page_num':range(1,page_num+1),
        'curr_page':page,
        'previous_page':previous_page,
        'next_page':next_page,
        'top4_article_list':top4_article_list
    })
    # render的作用就是将模板系统和数据进行渲染，并进行返回

# 接收requests参数，获取article_id传递到函数中
def get_detail_page(request,article_id):
    all_article = Article.objects.all()
    # 获取所有文章
    curr_article = None
    # 定义curr_article

    # 定义相关的变量
    previous_index = 0
    next_index = 0
    previous_article = None
    next_article = None
    for index,article in enumerate(all_article):
    # 遍历所有文章,获取对应的索引index
    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article)-1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
        # 当article_id相等时，赋值取出
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
            # 跳出循环
    section_list = curr_article.content.split('\n')
    # 将section_list以换行符切分，作用：换行
    return render(request, 'blog/detail.html', {
        'curr_article': curr_article,
        'section_list': section_list,
        'previous_article':previous_article,
        'next_article':next_article
    })
    # render的作用就是将模板系统和数据进行渲染，并进行返回



from django.shortcuts import render

# Create your views here.
USER_LIST = []
for i in range(999):
    temp = {'name': 'root' + str(i), 'age': 1}
    USER_LIST.append(temp)


def index(request):
    # 每页显示数量
    per_page_count = 10
    # 当前页
    current_page = int(request.GET.get('p'))

    start = (current_page - 1) * per_page_count
    end = current_page * per_page_count
    data = USER_LIST[start:end]
    if current_page < 1:
        prev_pager = 1
    else:
        prev_pager = current_page - 1

    next_pager = current_page + 1

    return render(request, 'index.html', {'users': data,
                                          'prev_pager': prev_pager,
                                          'next_pager': next_pager
                                          })


def index1(request):
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    # per_page 每页显示数量
    # count     数据总数量
    # num_pages 总页数
    # page_range 总页数索引范围
    # page      page对象
    paginator = Paginator(USER_LIST, 10)

    current_page = request.GET.get('p')
    try:
        posts = paginator.page(current_page)
        # has_next      是否有下一页
        # next_page_number  下一页页码
        # has_previous  是否有上一页
        # previous_page_number 上一页页码
        # object_list   分页之后数据列表，
        # number        当前页
        # paginator     paginator对象
    # 输入的页数不是数字，到第一页
    except PageNotAnInteger:
        posts = paginator.page(1)
    # 输入的页面超出实际页数，自动到最后一页
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index1.html',{'posts':posts})

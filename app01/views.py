from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CustonPaginator(Paginator):
    def __init__(self, current_page, per_page_num, *args, **kwargs):
        super(CustonPaginator, self).__init__(*args, **kwargs)
        # 当前页
        self.current_page = int(current_page)
        # 最多显示页码数量
        self.per_page_num = int(per_page_num)

    def pager_num_range(self):
        # 当前页
        # self.current_page
        # 最多显示的页码数量
        # self.per_page_num
        # 总页数
        # self.num_pages

        # 如果总页数小于显示页码数量
        if self.num_pages < self.per_page_num:
            return range(1, self.num_pages + 1)

        part = int(self.per_page_num / 2)
        # 如果总页数大于显示页码数量
        if self.current_page <= part:
            return range(1, self.per_page_num + 1)

        if (self.current_page + part) > self.num_pages:
            return range(self.num_pages - self.per_page_num, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)


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
    current_page = request.GET.get('p')
    # per_page 每页显示数量
    # count     数据总数量
    # num_pages 总页数
    # page_range 总页数索引范围
    # page      page对象
    paginator = CustonPaginator(current_page, 10, USER_LIST, 10)

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

    return render(request, 'index1.html', {'posts': posts})

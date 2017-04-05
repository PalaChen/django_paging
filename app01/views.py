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

    return render(request, 'index.html', {'users': data})

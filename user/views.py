from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import UserInfo
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def index(request):
    username = request.session.get('username')
    if username is not None and username.strip() != '':
        return render(request, 'login_success.html', {'username': username})
    else:
        return render(request, 'login.html')


@require_POST
def login(request):
    # 先获取参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 参数是否为空
    if username is None or username.strip() == '':
        context = {'usernamemessage': '用户名不能为空'}
        return render(request, 'login.html', context=context)
    if password is None or password.strip() == '':
        context = {'passwordmessage': '密码不能为空', 'username': username}
        return render(request, 'login.html', context=context)

    # 用户名和密码进行匹配（如果数据库中是加密的，那么匹配数据库时，需要对密码进行加密）
    try:
        user = UserInfo.objects.get(username=username, password=password)
    #  记住登录状态
        request.session['username'] = user.username
        request.session.set_expiry(10)
        # return render(request, 'login_success.html', {'username': username})
    #  重定向到首页，方便刷新，统一管理。
        return HttpResponseRedirect(redirect_to=reverse('user:index'))
    except UserInfo.DoesNotExist as e:
        context = {'message': '用户名或密码错误', 'username': username, 'password': password}
        return render(request, 'login.html', context)


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(redirect_to=reverse('user:index'))




from django.views.generic import View


#  基本视图
class UserView(View):
    http_method_names = ['get', 'post', 'head']

    def get(self, request, *args, **kwargs):
        #  '处理get请求'
        params = request.GET
        print('接入GET传入的参数:', params)
        return HttpResponse('处理一个get方法')

    def post(self, request, *args, **kwargs):
        print('接入POST请求传入的参数', request.POST)
        return HttpResponse('处理POST请求方法')

    def put(self, request, *args, **kwargs):
        params = request.body.decode(encoding='utf-8')
        print('接入PUT请求传入的参数')
        return HttpResponse('处理PUT请求方法')

    def delete(self, request, *agrs, **kwargs):
        params = request.body.decode(encoding='utf-8')
        print('接入Delete请求传入的参数')
        return HttpResponse('处理Delete请求方法')

    def http_method_not_allowed(self, request, *args, **kwargs):
        print('不允许传入的方法')
        return HttpResponse('不支持此 % s 方法' % request.method, status=405)


#  模板视图
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return {'users': UserInfo.objects.all()}


from django.views.generic.base import RedirectView


class UserRedirectView(RedirectView):
    # url = 'https://www.baidu.com'
    # permanent = True 为True时表示禁止重定向
    # query_string = True 允许跳转的url携带参数
    # pattern_name = 'user:home' 重定向采用反向查询
    pass


from django.views.generic.list import ListView


class UserListView(ListView):
    model = UserInfo
    # queryset = UserInfo.objects.filter(username__icontains='五')
    template_name = 'user_list.html'  # 指定模板名字，默认是小写应用名/小写model名_list.html
    # 指定遍历列表的key的名称，默认是objects_list
    # context_object_name = 'users'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     qs = UserInfo.objects.filter(username__icontains='五')
    #     return {'user': qs}
    paginate_by = 3


from django.views.generic.detail import DetailView


class UserDetailView(DetailView):
    model = UserInfo
    template_name = 'user_detail.html'


















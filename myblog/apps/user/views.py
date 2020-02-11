from django.shortcuts import render
from django.views import View

# Create your views here.

class Login(View):
    def get(self, request):
        # 返回登录界面
        return render(request, 'detail.html')

    def post(self, request):
        # 根据接收到的信息进行登录验证
        pass
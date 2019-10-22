from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def login(request):
    error_msg = ''
    if request.method == 'POST':
        email, pwd = request.POST.get('email'), request.POST.get('pwd')
        print(email, pwd)

        if email == 'lyysb@123.com' and pwd == '123':
            return redirect('/index/')
        else:
            error_msg = '邮箱或密码错误'

    return render(request, 'login.html', {'error_msg': error_msg})

def index(request):
    return render(request, 'index.html')





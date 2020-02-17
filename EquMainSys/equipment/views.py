from django.shortcuts import render,HttpResponse,redirect
from .models import *
import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth import authenticate, login, logout


# from django.forms import forms,fields,widgets
from django.forms import *
#
# class LoginForm(forms.Form):
#     # username=forms.charfiled
#     username = forms.CharField(label="用户名")
#     pwd= forms.CharField(lable="密码")
#     authority = forms.CharField(lable="权限")

# Create your views here.

#定义分页器
#
# def fenye(request,list,yeshu):
#     paginator = Paginator(list, yeshu)
#     pag_num = paginator.num_pages
#     curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
#     curuent_page = paginator.page(curuent_page_num)
#     if pag_num < 11:  # 判断当前页是否小于11个
#         pag_range = paginator.page_range
#     elif pag_num > 11:
#         if curuent_page_num < 6:
#             pag_range = range(1, 11)
#         elif curuent_page_num > (paginator.num_pages) - 5:
#             pag_range = range(pag_num - 9, pag_num + 1)
#         else:
#             pag_range = range(curuent_page_num - 5, curuent_page_num + 5)  # 当前页+5大于最大页数时
#     return



#首页的操作
#显示提醒事项以及显示维护员和设备的数量

def index(request):


    username = request.session.get('username', '')
    if not username:
        return render(request,'Login.html',{'msg':'请登陆！'})


    #获取维护员以及设备数量
    stulen=Stu.objects.all()
    stu_len=stulen.count()
    equlen=Equinfo.objects.all()
    equ_count=equlen.count()
    # print(equ_count)
    #获取提醒事项
    remind=Reminder.objects.order_by("-id")#倒序取出提醒事项
    recent=Recent.objects.order_by('-id')#倒序取出近期登陆情况

    rec = Paginator(recent,5)
    t_num = rec.num_pages
    c_page_num = int(request.GET.get('tpage', 1))  # 获取当前页数,默认为1
    c_page = rec.page(c_page_num)
    if t_num < 11:  # 判断当前页是否小于11个
        t_range = rec.page_range
    elif t_num > 11:
        if c_page_num < 6:
            t_range = range(1, 11)
        elif c_page_num > (rec.num_pages) - 5:
            t_range = range(t_num - 9, t_num + 1)
        else:
            t_range = range(c_page_num - 5, c_page_num + 5)  # 当前页+5大于最大页数时


    #分页
    paginator = Paginator(remind,5)
    pag_num = paginator.num_pages
    curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
    curuent_page = paginator.page(curuent_page_num)
    if pag_num < 11:  # 判断当前页是否小于11个
        pag_range = paginator.page_range
    elif pag_num > 11:
        if curuent_page_num < 6:
            pag_range = range(1, 11)
        elif curuent_page_num > (paginator.num_pages) - 5:
            pag_range = range(pag_num - 9, pag_num + 1)
        else:
            pag_range = range(curuent_page_num - 5, curuent_page_num + 5)  # 当前页+5大于最大页数时
    # print(type(remind.get(id=1).content))
    #进行分页操作
    #定义返回字典
    stat_content = {
            'username':username,
            'user_count': stu_len,
            'equ_count': equ_count,
            'remind_conn': remind,
            'recent_conn':recent,
            "pagintor" : paginator,
            "current_Page":curuent_page,
            "current_Page_num":curuent_page_num,
            "pag_range":pag_range,
            "recent": rec,
            "c_Page": c_page,
            "c_Page_num": c_page_num,
            "t_range": t_range
    }

    return render(request, 'index.html', stat_content)





def stuman(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})

    # stu_list=Stu.objects.order_by("-id")#倒序取出
    stu_list=Stu.objects.all().order_by('id')
    #分页操作
    paginator=Paginator(stu_list,6)
    pag_num = paginator.num_pages
    curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
    curuent_page = paginator.page(curuent_page_num)
    if pag_num < 11:  # 判断当前页是否小于11个
        pag_range = paginator.page_range
    elif pag_num > 11:
        if curuent_page_num < 6:
            pag_range = range(1, 11)
        elif curuent_page_num > (paginator.num_pages) - 5:
            pag_range = range(pag_num - 9, pag_num + 1)
        else:
            pag_range = range(curuent_page_num - 5, curuent_page_num + 5)  # 当前页+5大于最大页数时

    stu={"username":username,"stuli":stu_list,"pagintor" : paginator,"current_Page":curuent_page,"current_Page_num":curuent_page_num,"pag_range":pag_range}
    return render(request,"stuman.html",stu)


def adminman(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    # pass
    admin_list = Admin.objects.all().order_by('id')
    # 分页操作
    paginator = Paginator(admin_list, 6)
    pag_num = paginator.num_pages
    curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
    curuent_page = paginator.page(curuent_page_num)
    if pag_num < 11:  # 判断当前页是否小于11个
        pag_range = paginator.page_range
    elif pag_num > 11:
        if curuent_page_num < 6:
            pag_range = range(1, 11)
        elif curuent_page_num > (paginator.num_pages) - 5:
            pag_range = range(pag_num - 9, pag_num + 1)
        else:
            pag_range = range(curuent_page_num - 5, curuent_page_num + 5)  # 当前页+5大于最大页数时

    #修改用户信息
    # ch_user=request.POST.get('')

    adm = {"username":username,"admli": admin_list, "pagintor": paginator, "current_Page": curuent_page, "current_Page_num": curuent_page_num,
           "pag_range": pag_range}
    return render(request,"adminman.html",adm)
    # return redirect('/adminman/')


def adel(request):
    # return redirect('/index/adminman')
    adid=request.GET.get('nid')
    print(adid)
    Admin.objects.filter(id=adid).delete()
    # return render(request,'adminman.html')
    return redirect('/index/adminman')

def studel(request):
    stuid=request.GET.get('nid')
    print(stuid)
    Stu.objects.filter(id=stuid).delete()
    return redirect(('/index/stuman'))

def stuch(request):
    if request.method=='GET':
        return render(request,'stuman.html')
    else:
        userID=request.POST.get('usrID')
        pwd = request.POST.get('pwd')
        nid = request.POST.get('userid')
        userna = request.POST.get('userna')
        ret={'status':True,'errormsg':None}
        print(nid)
        print(userna)
        print(pwd)
        try:
            stu=Stu.objects.filter(id=nid).update(stuser=userID,stuname=userna,stpwd=pwd)
        except Exception as e:
            ret['status']=False
            ret['errormsg']=e
        return HttpResponse(str(ret))


def adch(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    if request.method=='GET':
        return render(request,'adminman.html')
    else:
        pwd = request.POST.get('pwd')
        nid = request.POST.get('userid')
        userna = request.POST.get('userna')
        ret={'status':True,'errormsg':None}
        print(nid)
        print(userna)
        print(pwd)
        try:
            Adch = Admin.objects.filter(id=nid).update(aduser=userna,adpwd=pwd)
        except Exception as e:
            ret['status']=False
            ret['errormsg']='处理异常，请重试！'
        return HttpResponse(str(ret))
        # return HttpResponse(str(ret))
        # return render(request,'adminman.html')


def adsearch(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    name=request.GET.get('user')
    ad_list=Admin.objects.filter(aduser=name)
    paginator = Paginator(ad_list, 10)
    pag_num = paginator.num_pages
    curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
    curuent_page = paginator.page(curuent_page_num)
    if pag_num < 11:  # 判断当前页是否小于11个
        pag_range = paginator.page_range
    elif pag_num > 11:
        if curuent_page_num < 6:
            pag_range = range(1, 11)
        elif curuent_page_num > (paginator.num_pages) - 5:
            pag_range = range(pag_num - 9, pag_num + 1)
        else:
            pag_range = range(curuent_page_num - 5, curuent_page_num + 5)
    stat = {
        'username': username,
        'man_list': ad_list,
        "pagintor": paginator,
        "current_Page": curuent_page,
        "current_Page_num": curuent_page_num,
        "pag_range": pag_range
    }
    return render(request, 'adminman.html', stat)




def addadmin(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    if request.method=='GET':
        return render(request,'addadmin.html',{'username':username})
    else:
        stat={'msg':None,'username':username}
        uflag=0
        nid=request.POST.get('userid')
        u=request.POST.get('userna')
        p=request.POST.get('userpwd')
        pp=request.POST.get('userpwdd')
        a=request.POST.get('select')
        if p==pp:
            if not u:
                uflag=1
            elif " " in u or " " in p:
                uflag=2
            elif not nid:
                uflag=3
        else:
            stat['msg']='两次密码不一致！'
            return  render(request,'addadmin.html',stat)

        if uflag==1:
            stat['msg'] = '用户名不能为空！'
            return render(request, 'addadmin.html', stat)
        elif uflag==2:
            stat['msg']='用户名或密码不能包含空格！'
            return render(request,'addadmin.html',stat)
        elif uflag==3:
            stat['msg'] = '用户工号不能为空！'
            return render(request, 'addadmin.html', stat)
        try:
            admin=Admin.objects.create(adid=nid,aduser=u,adpwd=p,authority=a)
            return redirect('/index/adminman')
        except Exception as e:
            return render(request,'addadmin.html',{'msg':'处理异常，请重试！'})

def addstu(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    if request.method == 'GET':
        return render(request, 'addstu.html', {'username': username})
    else:
        stat = {'msg': None, 'username': username}
        uflag = 0
        usrid=request.POST.get('userID')
        u = request.POST.get('userna')
        p = request.POST.get('userpwd')
        pp = request.POST.get('userpwdd')
        if p == pp:
            if not u:
                uflag = 1
            elif " " in u or " " in p or " " in usrid:
                uflag = 2
        else:
            stat['msg'] = '两次密码不一致！'
            return render(request, 'addstu.html', stat)

        if uflag == 1:
            stat['msg'] = '用户名不能为空！'
            return render(request, 'addstu.html', stat)
        elif uflag == 2:
            stat['msg'] = '字段不能包含空格！'
            return render(request, 'addstu.html', stat)
        # d=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(usrid+u+p+pp)
        stu=Stu.objects.create(stuname=u,stpwd=p,stuser=usrid)
        return redirect('/index/stuman')

def stusearch(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    name=request.GET.get('user')
    stu_list=Stu.objects.filter(stuname=name)
    paginator = Paginator(stu_list, 10)
    pag_num = paginator.num_pages
    curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
    curuent_page = paginator.page(curuent_page_num)
    if pag_num < 11:  # 判断当前页是否小于11个
        pag_range = paginator.page_range
    elif pag_num > 11:
        if curuent_page_num < 6:
            pag_range = range(1, 11)
        elif curuent_page_num > (paginator.num_pages) - 5:
            pag_range = range(pag_num - 9, pag_num + 1)
        else:
            pag_range = range(curuent_page_num - 5, curuent_page_num + 5)
    stat = {
        'username': username,
        'man_list': stu_list,
        "pagintor": paginator,
        "current_Page": curuent_page,
        "current_Page_num": curuent_page_num,
        "pag_range": pag_range
    }
    return render(request, 'stuman.html', stat)

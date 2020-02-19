from django.shortcuts import render,HttpResponse,redirect
from .models import *
import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from equipment import views



###################处理近期登陆情况#####################
def recent(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    rec=Recent.objects.order_by('-id')
    stat_content=views.fenye(request,rec,10)
    stat_content['username']=username
    # paginator = Paginator(rec, 10)
    # pag_num = paginator.num_pages
    # curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
    # curuent_page = paginator.page(curuent_page_num)
    # # print(curuent_page)
    # if pag_num < 11:  # 判断当前页是否小于11个
    #     pag_range = paginator.page_range
    # elif pag_num > 11:
    #     if curuent_page_num < 6:
    #         pag_range = range(1, 11)
    #     elif curuent_page_num > (paginator.num_pages) - 5:
    #         pag_range = range(pag_num - 9, pag_num + 1)
    #     else:
    #         pag_range = range(curuent_page_num - 5, curuent_page_num + 5)  # 当前页+5大于最大页数时
    # # print(type(remind.get(id=1).content))
    # # 进行分页操作
    # # 定义返回字典
    # stat_content = {'username': username,  "pagintor": paginator, "current_Page": curuent_page,
    #                 "current_Page_num": curuent_page_num, "pag_range": pag_range}

    return render(request,'recent.html',stat_content)

def recentdel(request):
    nid=request.GET.get('nid')
    rc=Recent.objects.filter(id=nid).delete()
    return redirect('/index/recent/')


def recentsearch(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    user=request.GET.get('username')
    rec=Recent.objects.filter(username=user)
    stat_content=views.fenye(request,rec,10)
    stat_content['username']=username
    # paginator = Paginator(rec, 10)
    # pag_num = paginator.num_pages
    # curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
    # curuent_page = paginator.page(curuent_page_num)
    # # print(curuent_page)
    # if pag_num < 11:  # 判断当前页是否小于11个
    #     pag_range = paginator.page_range
    # elif pag_num > 11:
    #     if curuent_page_num < 6:
    #         pag_range = range(1, 11)
    #     elif curuent_page_num > (paginator.num_pages) - 5:
    #         pag_range = range(pag_num - 9, pag_num + 1)
    #     else:
    #         pag_range = range(curuent_page_num - 5, curuent_page_num + 5)  # 当前页+5大于最大页数时
    # # print(type(remind.get(id=1).content))
    # # 进行分页操作
    # # 定义返回字典
    # stat_content = {'username': username, "pagintor": paginator, "current_Page": curuent_page,
    #                 "current_Page_num": curuent_page_num, "pag_range": pag_range}

    return render(request, 'recent.html', stat_content)

###################处理提醒事项#####################

def remindman(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})

    rem_list = Reminder.objects.order_by('-id')
    stat_content=views.fenye(request,rem_list,10)
    stat_content['username']=username


    # paginator = Paginator(rem_list, 10)
    # pag_num = paginator.num_pages
    # curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
    # curuent_page = paginator.page(curuent_page_num)
    # # print(curuent_page)
    # if pag_num < 11:  # 判断当前页是否小于11个
    #     pag_range = paginator.page_range
    # elif pag_num > 11:
    #     if curuent_page_num < 6:
    #         pag_range = range(1, 11)
    #     elif curuent_page_num > (paginator.num_pages) - 5:
    #         pag_range = range(pag_num - 9, pag_num + 1)
    #     else:
    #         pag_range = range(curuent_page_num - 5, curuent_page_num + 5)  # 当前页+5大于最大页数时
    # # print(type(remind.get(id=1).content))
    # # 进行分页操作
    # # 定义返回字典
    # stat_content = {'username': username, 'rem_list': rem_list, "pagintor": paginator, "current_Page": curuent_page,
    #                 "current_Page_num": curuent_page_num, "pag_range": pag_range}

    return render(request, 'remindman.html', stat_content)


def remindch(request):
    nid=request.POST.get('nid')
    content=request.POST.get('content')
    print(nid)
    print(content)
    rem=Reminder.objects.filter(id=nid).update(content=content)
    return HttpResponse('ok')

def remindel(request):
    nid=request.GET.get('nid')
    rem=Reminder.objects.filter(id=nid).delete()
    return redirect('/index/remindman/')

def addremind(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    if request.method=='GET':
        return render(request,'addremind.html',{'username':username})
    d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    content=request.POST.get('content')
    if not content:
        return render(request,'addremind.html',{'msg':'字段不能为空！'})
    try:
        rem=Reminder.objects.create(date=d,who=username,content=content)
        return redirect('/index/remindman/')
    except Exception as e:

        return render(request,'addremind.html',{'msg':'处理异常！'})

def remindsearch(request):
    username = request.session.get('username', '')
    if not username:
        return render(request, 'Login.html', {'msg': '请登陆！'})
    searchd=request.GET.get('date')
    # print(searchd)
    rem=Reminder.objects.filter(date__contains=searchd)

    stat_content=views.fenye(request,rem,10)
    stat_content['username']=username

    # paginator = Paginator(rem, 10)
    # pag_num = paginator.num_pages
    # curuent_page_num = int(request.GET.get('page', 1))  # 获取当前页数,默认为1
    # curuent_page = paginator.page(curuent_page_num)
    # # print(curuent_page)
    # if pag_num < 11:  # 判断当前页是否小于11个
    #     pag_range = paginator.page_range
    # elif pag_num > 11:
    #     if curuent_page_num < 6:
    #         pag_range = range(1, 11)
    #     elif curuent_page_num > (paginator.num_pages) - 5:
    #         pag_range = range(pag_num - 9, pag_num + 1)
    #     else:
    #         pag_range = range(curuent_page_num - 5, curuent_page_num + 5)  # 当前页+5大于最大页数时
    # # print(type(remind.get(id=1).content))
    # # 进行分页操作
    # # 定义返回字典
    # stat_content = {'username': username,  "pagintor": paginator, "current_Page": curuent_page,
    #                 "current_Page_num": curuent_page_num, "pag_range": pag_range}

    return render(request, 'remindman.html', stat_content)
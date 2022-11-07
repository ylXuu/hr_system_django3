import datetime

from django.shortcuts import render, redirect
from . import funcs

# Create your views here.

def login(request):
    if request.session.get('is_login', None):
        return redirect('/home/')
    return render(request, 'login.html', {'error':False})

def logout(request):
    if request.session.get('is_login', None):
        request.session.flush()
        return redirect('/login/')

def register(request):
    if request.session.get('is_login', None):
        return redirect('/home/')
    return render(request, 'register.html')

def register_confirm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = funcs.find_user(name)
        print(user)
        if user:
            return render(request, 'register.html', {'error':0})
        if password1 != password2:
            return render(request, 'register.html', {'error':1})
        if funcs.add_user(name, password1):
            return redirect('/login/')
        else:
            return render(request, 'register.html', {'error':2})

def forget(request):
    pass

def home(request):
    if request.session.get('is_login', None):
        return render(request, 'home.html', {'cur':0})
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = funcs.find_name_password(name, password)
        if user:
            request.session['is_login'] = True
            request.session['name'] = user[0][0]
            request.session['password'] = user[0][1]
            return render(request, 'home.html', {'cur':0})
        else:
            return render(request, 'login.html', {'error':True})
    else:
        return redirect('/login/')


def worker(request):
    if request.session.get('is_login', None):
        result = funcs.find_all_workers()
        workers, idx = [], 1
        for i in result:
            data = {'idx': idx, 'worker_id': i[0], 'worker_name': i[1],
                    'worker_sex': '男' if i[2] else '女', 'worker_age': i[3],
                    'worker_department': i[4], 'worker_position': i[5],
                    'worker_phone': i[6], 'worker_entry_time': i[7]}
            workers.append(data)
            idx += 1
        return render(request, 'worker.html', {'workers':workers, 'cur':1})
    else:
        return redirect('/login/')

def department(request):
    if request.session.get('is_login', None):
        return render(request, 'department.html', {'cur':2})
    else:
        return redirect('/login/')

def training(request):
    if request.session.get('is_login', None):
        return render(request, 'training.html', {'cur':3})
    else:
        return redirect('/login/')

def recruitment(request):
    if request.session.get('is_login', None):
        return render(request, 'recruitment.html', {'cur':4})
    else:
        return redirect('/login/')

def salary(request):
    if request.session.get('is_login', None):
        return render(request, 'salary.html', {'cur':5})
    else:
        return redirect('/login/')

def reward(request):
    if request.session.get('is_login', None):
        return render(request, 'reward.html', {'cur':6})
    else:
        return redirect('/login/')

def account(request):
    if request.session.get('is_login', None):
        return render(request, 'account.html', {'cur':7})
    else:
        return redirect('/login/')


def worker_query(request):
    if request.method == 'POST':
        attribute = request.POST.get('attribute')
        option = request.POST.get('option')
        workers, result = [], []
        if option == 'option1':
            result = funcs.find_worker_by_name(attribute)
        elif option == 'option2':
            result = funcs.find_worker_by_department(attribute)
        elif option == 'option3':
            result = funcs.find_worker_by_position(attribute)
        idx = 1
        for i in result:
            data = {'idx': idx, 'worker_id': i[0], 'worker_name': i[1],
                    'worker_sex': '男' if i[2] else '女', 'worker_age': i[3],
                    'worker_department': i[4], 'worker_position': i[5],
                    'worker_phone': i[6], 'worker_entry_time': i[7]}
            workers.append(data)
            idx += 1
        return render(request, 'worker.html', {'workers':workers, 'cur':1})

def worker_add(request):
    if request.session.get('is_login', None):
        return render(request, 'worker_add.html', {'cur':1})
    else:
        return redirect('/login/')

def worker_add_confirm(request):
    if request.method == 'POST':
        # TODO: 要做合法性检验
        worker_id = request.POST.get('worker_id')
        worker_name = request.POST.get('worker_name')
        worker_sex = int(request.POST.get('worker_sex'))
        worker_age = int(request.POST.get('worker_age'))
        worker_department_t = int(request.POST.get('worker_department'))
        worker_department = None
        if worker_department_t == 0:
            worker_department = '技术部'
        elif worker_department_t == 1:
            worker_department = '财务部'
        elif worker_department_t == 2:
            worker_department = '后勤部'
        elif worker_department_t == 3:
            worker_department = '其他'
        worker_position = request.POST.get('worker_position')
        worker_phone = request.POST.get('worker_phone')
        if funcs.add_worker(worker_id, worker_name, worker_sex, worker_age, worker_department, worker_position, worker_phone):
            return redirect('/worker/')
        else:
            return redirect('/worker/')

def worker_modify(request, id):
    # Todo
    pass

def worker_delete(request, id):
    if funcs.delete_worker(id):
        return redirect('/worker/')
    else:
        return redirect('/worker/')




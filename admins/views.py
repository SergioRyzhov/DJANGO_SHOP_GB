from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'title': 'Geekshop - Админ Панель'}
    return render(request, 'admins/index.html', context)


# create
def admin_users_create(request):
    context = {'title': 'Geekshop - Создание пользователей'}
    return render(request, 'admins/admin-users-create.html', context)


# read
def admin_users(request):
    context = {'title': 'Geekshop - Пользователи'}
    return render(request, 'admins/admin-users-read.html', context)


# update
def admin_users_update(request):
    context = {'title': 'Geekshop - Обновление пользователя'}
    return render(request, 'admins/admin-users-update-delete.html', context)


# delete
def admin_users_delete(request):
    pass
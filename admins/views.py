from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm

# Create your views here.
def index(request):
    context = {'title': 'Geekshop - Админ Панель'}
    return render(request, 'admins/index.html', context)


# create
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Geekshop - Создание пользователей', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


# read
def admin_users(request):
    context = {
        'title': 'Geekshop - Пользователи',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


# update
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES,  data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Geekshop - Обновление пользователя',
        'form': form,
        'selected_user': selected_user,
        }
    return render(request, 'admins/admin-users-update-delete.html', context)


# delete
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.save_delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))
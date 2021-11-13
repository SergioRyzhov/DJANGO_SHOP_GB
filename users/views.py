from basket.models import Basket
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
from django.utils.timezone import now
from geekshop.settings import DOMAIN_NAME, EMAIL_HOST_USER
from users.models import User

from users.forms import UserLoginForm, UserRegistrationForm, UsersProfileForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'GeekShop - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                messages.success(request, 'Сообщение пользователю отправлено\nВы успешно зарегестрировались')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                messages.success(request, 'Сообщение пользователю не отправлено\nВы успешно зарегестрировались')
                return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UsersProfileForm(instance=user, files=request.FILES,  data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно изменены')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UsersProfileForm(instance=user)

    # baskets = Basket.objects.filter(user=user) 
    context = {
        'title': 'GeekShop - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=user),
        # 'total_quantity': sum(basket.quantity for basket in baskets),
        # 'total_sum': sum(basket.sum() for basket in baskets),
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'users/verify.html')
        else:
            messages.error(request, f'error activation user: {user}')
            return render(request, 'users/verify.html')
    except Exception as err:
        messages.error(request, f'error activation user: {err.args}')
        return HttpResponseRedirect(reverse('users:profile'))

def send_verify_mail(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    
    title = f'Подтвердите учетную запись {user.username}'
    
    message = f'Для подтверждения учетной записи {user.username}'   \
            f'на портале {DOMAIN_NAME} перейдите по ссылке '    \
            f'{DOMAIN_NAME}{verify_link}'
            
    return send_mail(title, message, EMAIL_HOST_USER, [user.email], fail_silently=False)

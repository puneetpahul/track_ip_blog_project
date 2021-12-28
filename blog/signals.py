from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender = User)
def login_success(sender,request,user,**kwargs):
    print('******************************')
    print('logged in signal.. run intro')
    ip = request.META.get('REMOTE_ADDR')
    print('client ip :::::',ip)
    request.session['ip'] = ip

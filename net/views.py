from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render

from net.friends.models import User


def test_login(request):
    me, _ = User.objects.get_or_create(name='Iroh', email='iroh@example.com')
    me.set_password('test')
    me.save()

    me = authenticate(username='iroh@example.com', password='test')
    if not me:
        raise Exception("Failed to login Iroh.")
    login(request, me)

    return redirect('/feed/')


def basic_view(name):
    def view(request):
        return render(request, name + '.html')

    view.__name__ = name
    return view

from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render

from net.friends.models import User


def test_login(request):
    iroh = User.objects.get(email='iroh@example.com')
    iroh.set_password('test')
    iroh.save()

    iroh = authenticate(username='iroh@example.com', password='test')
    if not iroh:
        raise Exception("Failed to login Iroh.")
    login(request, iroh)

    return redirect('/feed/')


def generic_view(name):
    def view(request):
        return render(request, name + '.html', {
            'request': request,
        })

    view.__name__ = name
    return view


def profile(request, pk=None):
    if pk is None:
        raise Exception('pk not provided')

    user = User.objects.get(pk=pk)

    followed = request.user.subscriptions.filter(to_user=user).exists()

    return render(request, 'profile.html', {
        'request': request,
        'user': user,
        'followed': followed,
    })

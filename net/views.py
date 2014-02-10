import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import redirect, render

from net.forms import ProfileForm
from net.models import User


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


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile/' + str(request.user.pk))
        else:
            return HttpResponse(json.dumps(form.errors))
    elif request.method == 'GET':
        return generic_view('edit_profile')(request)
    else:
        raise Exception('Invalid request method.')

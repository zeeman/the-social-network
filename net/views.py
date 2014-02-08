from django.shortcuts import render


def basic_view(name):
    def view(request):
        return render(request, name + '.html')

    view.__name__ = name
    return view

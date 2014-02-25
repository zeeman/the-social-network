from django.http import HttpResponse


def first(qs):
    return next(iter(qs), None)


class HttpResponse422(HttpResponse):
    status_code = 422

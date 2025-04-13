from django.http import HttpResponse


def django_greetings(request) -> HttpResponse:
    return HttpResponse(
        "<h1>Greetings from the Django APP!!! :)</h1>"
    )

def django_greetings_user(request, name) -> HttpResponse:
    return HttpResponse(
        f"<h1>Hello, {name}!!!</h1>"
    )
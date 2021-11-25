from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse


@require_http_methods(["POST"])
def box_test(request):
    data = request.body.decode()

    return HttpResponse(data)









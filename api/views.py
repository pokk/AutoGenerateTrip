from django.http import JsonResponse
from django.shortcuts import render_to_response

# Create your views here.
from django.views import View


class Login(View):
    def get(self, request):
        print(3333, request.GET['id'])
        return render_to_response('login/login.html', locals())

    def post(self, request):
        return JsonResponse({'id': 'hello', 'vf': 123})


def test(request):
    print(request.GET.get('id'))
    return render_to_response('login/login.html', locals())

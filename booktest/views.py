from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # return HttpResponse("这是booktest应用的index")
    print("---------index---------------")
    # raise Exception("自定义异常")
    return render(request, "booktest/index.html")


def static_test(request):
    return render(request, "booktest/static_test.html")

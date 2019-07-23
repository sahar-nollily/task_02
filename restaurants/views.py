from django.shortcuts import render

# Create your views here.
def test(request):
    context = {
        "msg": "Hello World!",
    }

    return render(request,'file.html',context)

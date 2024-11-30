from django.shortcuts import render

# Create your views here.

def about(request):
    template = 'homepage/index.html'
    return render(request, template)
def rules(request):
    template = 'homepage/index.html'
    return render(request, template)

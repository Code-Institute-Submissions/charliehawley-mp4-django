from django.shortcuts import render

# Create your views here.
def go_home(request):
    return render(request, 'wisecrack/wisecrack.html')
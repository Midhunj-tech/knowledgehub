from django.shortcuts import render

def signin_view(request):
    return render(request, 'signin.html')
def signup_view(request):
    return render(request,'signup.html')

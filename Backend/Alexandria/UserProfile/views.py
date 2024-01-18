from django.shortcuts import render, redirect
from .models import UserAlexandria, AdditionalInfoUA

def authentication(request):
    return render(request, 'UserProfile/authorization.html')


def registration_view(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        birth_date = request.POST.get('birth_date')
        fathername = request.POST.get('fathername')

        user = UserAlexandria.objects.create_user(
            name=name, 
            surname=surname, 
            fathername = fathername,
            birth_date = birth_date, 
            email=email,
            username = username,
            password=password, 
        )
        
        additional_info = AdditionalInfoUA.objects.create(user=user, point=0, money=0)

        return redirect('UserProfile/temp.html')

    return render(request, 'UserProfile/temp.html')

from django.shortcuts import render
from datetime import date

def my_page(request):
    first_name = "Gleb"
    last_name = "Kls"
    birth_date = date(2005, 5, 15)  
    email = "example@gmail.com"

    # Обчислення віку
    today = date.today()
    age = today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "birth_date": birth_date,
        "age": age,
        "email": email,
    }
    return render(request, "myapp/mypage.html", context)

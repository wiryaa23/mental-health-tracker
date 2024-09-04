from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152115',
        'name': 'Wirya Dharma Kurnia',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

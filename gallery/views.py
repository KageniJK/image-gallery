from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture


# Create your views here.
def landing(request):
    pics = Picture.all_pics()
    return render(request, "landing.html", {'pics': pics})


def search_results(request):
    if 'pic' in request.GET and request.GET['pic']:
        search_term = request.GET.get('pic')
        searched_pics = Picture.search_picture(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'pics': searched_pics})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})
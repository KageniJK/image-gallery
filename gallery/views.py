from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Picture, Location


# Create your views here.
def landing(request):
    pics = Picture.all_pics()
    locations = Location.objects.all()
    return render(request, "index.html", {'pics': pics, 'locations': locations})


def search_results(request):
    locations = Location.objects.all()
    if 'pic' in request.GET and request.GET['pic']:
        search_term = request.GET.get('pic')
        searched_pics = Picture.search_picture(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'pics': searched_pics, 'locations': locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message, 'locations': locations})


def location(request, location):
    locations = Location.objects.all()
    try:
        pics = Picture.filter_by_loc(location)
    except Picture.DoesNotExist:
        raise Http404()

    return render(request, 'location.html', {'pics': pics, 'locations': locations})
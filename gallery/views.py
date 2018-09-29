from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Picture, Location,Category


# Create your views here.
def landing(request):
    pics = Picture.all_pics()
    locations = Location.objects.all()
    return render(request, "index.html", {'pics': pics, 'locations': locations})


def search_results(request):
    locations = Location.objects.all()
    if 'pic' in request.GET and request.GET['pic']:
        search_term = request.GET.get('pic')
        searched_cats = Category.search_category(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'cats': searched_cats, 'locations': locations})

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


def category(request, category):
    locations = Location.objects.all()
    try:
        pics = Picture.filter_by_cat(category)
    except Picture.DoesNotExist:
        raise Http404()

    return render(request, 'location.html', {'pics': pics, 'locations': locations})
from django.shortcuts import render


def page_not_found_view(request, exception):
    return render(request, 'product/404.html', status=404)
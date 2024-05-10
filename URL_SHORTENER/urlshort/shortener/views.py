from django.shortcuts import render, redirect
from . models import Url
from . forms import UrlForm
import shortuuid


# Create your views here.

def index(request):
    form = UrlForm(request.POST or None)
    if form.is_valid():
        long_url = form.cleaned_data['original']
        custom = form.cleaned_data['custom']
        short = shortuuid.uuid()
        new_url = Url.objects.create(original=long_url, short=short, custom=custom)
        return redirect('shortened_url', short_code=short)
    context = {'form': form}
    return render(request, 'index.html', context)

def redirect_original_url(request):
    try:
        url_obj = Url.objects.get('short')
        return redirect(url_obj)
    except Url.DoesNotExist:
        return render(request, 'error.html')

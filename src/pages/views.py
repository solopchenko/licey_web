from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404


from .models import Page

# Create your views here.
class PageView(View):
    def get(self, request, page_url, *args, **kwargs):

        page = get_object_or_404(Page, url=page_url)
        context = {'page': page}
        template = 'page.html'

        return render(request, template, context)
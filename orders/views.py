from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import View

from .models import PSAccount


class Index(View):

    def get(self, request):
        queryset = PSAccount.objects.all()
        paginator = Paginator(queryset, 10)  # Show orders number
        page = request.GET.get('page')
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            orders = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            orders = paginator.page(paginator.num_pages)
        return render(request, 'orders/index.html', {'orders': orders})

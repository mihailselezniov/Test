from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from list_of_discounts.models import Store_lists_of_discounts

import json
from grab import Grab

class MainPageListOfDiscounts(generic.ListView):
    template_name = 'list_of_discounts/fresh_list_of_discounts.html'
    context_object_name = 'fresh_list_of_discounts'
    def get_queryset(self):
        """
        Returns the last twenty stored data.
        """
        return Store_lists_of_discounts.objects.all().order_by('-date_save')[:20]

class ListOfDiscountsView(generic.DetailView):
    model = Store_lists_of_discounts
    template_name = 'list_of_discounts/view_list_of_discounts.html'
    def get_object(self):
        """
        Returns details of stored data.
        """
        object = super(ListOfDiscountsView, self).get_object()
        object.data = json.loads(object.data)
        return object

def take_data(request):
    """
    Stores the data if they are new.
    """
    url = "https://modnakasta.ua"
    page = Grab()
    page.go(url)
    discount = map(lambda x: x.text, page.xpath_list("//div[@class='column_discount']"))
    title = map(lambda x: x.text, page.xpath_list("//div[@class='column_title']"))
    category = map(lambda x: x.text, page.xpath_list("//div[@class='column_category']"))
    data = []
    for i in range(len(discount)):
        data.append({"discount": discount[i], "title": title[i], "category": category[i]})
    data = json.dumps(data)
    if not data == Store_lists_of_discounts.objects.order_by('-date_save')[0].data:
        dataObject = Store_lists_of_discounts(data=data, date_save=timezone.now())
        dataObject.save()
    return HttpResponseRedirect(reverse('list_of_discounts:main_page_list_of_discounts'))
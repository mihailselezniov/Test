from django.conf.urls import patterns, url

from list_of_discounts import views

urlpatterns = patterns('',
    url(r'^$', views.MainPageListOfDiscounts.as_view(), name='main_page_list_of_discounts'),
    url(r'^(?P<pk>\d+)/$', views.ListOfDiscountsView.as_view(), name='list_of_discounts_view'),
    url(r'^take_data/$', views.take_data, name='take_list_of_discounts'),
)
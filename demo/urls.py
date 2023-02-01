from django.urls import path

from . import views

urlpatterns = [
    path("countries/", views.ListCountryView.as_view(), name="list_countries"),
    path("sectors/", views.ListSectorsView.as_view(), name="list_sectors"),
    path("loans/", views.ListAllLoans.as_view(), name="list_loans"),
    path("excel/", views.GenerateExcel.as_view(), name="generate_excel"),
]

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from django.http import HttpResponse
from django.db.models import Sum, Count

from .models import Loan, Sector, Country
from .serializers import LoanSerializer, CountrySerializer, SectorSerializer
from .excel_service import generate_excel_sheet


class ListCountryView(ListAPIView):
    serializer_class = CountrySerializer

    def get(self, request):
        country = Country.objects.all()
        country_data = []
        for c in country:
            country_data.append(str(c))

        return Response(status=200, data={"countries": country_data})


class ListSectorsView(ListAPIView):
    serializer_class = SectorSerializer

    def get(self, request):
        sectors = Sector.objects.all()
        sectors_data = []
        for s in sectors:
            sectors_data.append(str(s))

        return Response(status=200, data={"sectors": sectors_data})


class ListAllLoans(ListAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class GenerateExcel(ListAPIView):

    def get(self, request):
        excel_data = Loan.objects.select_related("country", "sector", "currency").all()

        by_year = excel_data.values("signature_date__year").annotate(
            total_amount=Sum("signed_amount"),
            count=Count("uuid"),
        )

        by_country = excel_data.values("country__name").annotate(
            total_amount=Sum("signed_amount"),
            count=Count("uuid"),
        )

        by_sector = excel_data.values("sector__name").annotate(
            total_amount=Sum("signed_amount"),
            count=Count("uuid"),
        )

        excel_output = generate_excel_sheet(excel_data, by_year, by_country, by_sector)

        filename = "api_sheet.xlsx"
        response = HttpResponse(
            excel_output,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = "attachment; filename=%s" % filename
        return response

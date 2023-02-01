from django.db import models
import uuid


class Sector(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Currency(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=10, default="Euro")
    symbol = models.CharField(max_length=10, default="€")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Currencies"


class Loan(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    signature_date = models.DateField()
    title = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    signed_amount = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.title

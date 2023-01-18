from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
from myap.models import Currency, Holding
class HoldingInLine(admin.TabularInline):
    fields = ('iso','value','buy_data')
    model = Holding
    extra = 0
class CurrencyAdmin(admin.ModelAdmin):
    fields = ('long_name','iso')
    inlines = [HoldingInLine]
admin.site.register(Currency,CurrencyAdmin)
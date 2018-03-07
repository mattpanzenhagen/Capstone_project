from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from hickory_theatre.models import Advertisments, MailingList, Producermasterdatabase


@admin.register(Advertisments)
class AdvertismentsAdmin(ImportExportModelAdmin):
	list_display = [f.name for f in Advertisments._meta.fields]
	search_fields = ['first_name', 'last_name', 'company_name']
	
#admin.site.register(Advertisments),
@admin.register(MailingList)
class MailingListAdmin(ImportExportModelAdmin):
	list_display = [f.name for f in MailingList._meta.fields]
	search_fields = ['fname', 'lname']
@admin.register(Producermasterdatabase)
class ProducermasterdatabaseAdmin(ImportExportModelAdmin):
	list_display = [f.name for f in Producermasterdatabase._meta.fields]
	search_fields = ['company_name', 'contact_person']
	
	
	

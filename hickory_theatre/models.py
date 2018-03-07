from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Advertisments(models.Model):
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    first_name = models.TextField(db_column='First Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    last_name = models.TextField(db_column='Last Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    company_name = models.TextField(db_column='Company Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    address_line_1 = models.TextField(db_column='Address Line 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    address_line_2 = models.TextField(db_column='Address Line 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zip_code = models.TextField(db_column='ZIP Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    home_phone = models.TextField(db_column='Home Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    work_phone = models.TextField(db_column='Work Phone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    last_advertised = models.TextField(db_column='Last Advertised', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    customer_type = models.TextField(db_column='Customer Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    ad_size = models.TextField(db_column='Ad Size', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    color = models.TextField(db_column='Color', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    placement = models.TextField(db_column='Placement', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    e_mail_address = models.TextField(db_column='E-mail Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    renewaldate = models.TextField(db_column='RenewalDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    new_copy = models.TextField(db_column='New Copy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    commission = models.TextField(db_column='Commission', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    price = models.TextField(db_column='Price', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ad_page = models.TextField(db_column='Ad Page', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
       # managed = False
        db_table = 'Advertisments'
        verbose_name = 'Advertisment'


class MailingList(models.Model):
    lname = models.TextField(db_column='LNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fname = models.TextField(db_column='FNAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mrg = models.TextField(db_column='MRG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pobox = models.TextField(db_column='POBOX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    addr = models.TextField(db_column='ADDR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='CITY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zip = models.TextField(db_column='ZIP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hphone = models.TextField(db_column='HPHONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wphone = models.TextField(db_column='WPHONE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    function = models.TextField(db_column='FUNCTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    prem_sub_current_year = models.TextField(db_column='Prem Sub current year', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    prem_sub_last_year = models.TextField(db_column='Prem Sub last year', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    prem_level = models.TextField(db_column='Prem level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    prod_invt = models.TextField(db_column='Prod invt', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    isbusnmember = models.TextField(db_column='IsBusnMember', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    busn_level = models.TextField(db_column='Busn Level', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    is_cvcc_seas_tix = models.TextField(db_column='Is CVCC seas tix', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    yta = models.TextField(db_column='YTA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fk_list = models.TextField(db_column='FK LIST', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    vac_extr = models.TextField(db_column='VAC EXTR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    seller = models.TextField(db_column='Seller', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    board = models.TextField(db_column='Board', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actor = models.TextField(db_column='Actor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    guild = models.TextField(db_column='Guild', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    donor = models.TextField(db_column='Donor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
       # managed = False
        db_table = 'Mailing_List'
        verbose_name = 'Mailing List'


class Producermasterdatabase(models.Model):
    company_name = models.TextField(db_column='Company Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    contact_person = models.TextField(db_column='Contact Person', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    has_produced_field = models.TextField(db_column='has produced?', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zip = models.TextField(db_column='Zip', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ph = models.TextField(db_column='PH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    number_2nd_contact_s_field = models.TextField(db_column='2nd contact(s)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    physical_address = models.TextField(db_column='Physical Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    likely_options = models.TextField(db_column='Likely Options', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
       # managed = False
        db_table = 'ProducerMasterDatabase'
        verbose_name = 'Producer Master'




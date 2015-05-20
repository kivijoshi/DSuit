from django.contrib import admin
from django import forms
from DoctorsCompanion.models import PatientsRec,VisitsRec,MedicineRec,FinancialRecord,TimingsRec,BillingsRec
from django.http import HttpResponse
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
from django.http import HttpResponse
from django.forms import TextInput, Textarea
from django.forms import Select
from datetime import datetime
from django.db import models
from django.forms import ModelForm, Textarea
from django.contrib import messages
import datetime
from django.conf.urls import patterns, url

from django.shortcuts import render

class FinancialOverviewForm(forms.Form):
	Overview_From = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
	Overview_Until = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
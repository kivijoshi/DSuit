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
#from DoctorsCompanion.models import DemoModel
import webcam.admin
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from webcam import widgets
from webcam.fields import CameraField

FORMFIELD_FOR_DBFIELD_DEFAULTS[CameraField] = {'widget': widgets.CameraWidget}

class VisitsRecForm(ModelForm):
    class Meta:
        model = VisitsRec
        widgets = {
            "Patient_Visit_Complaint": Textarea(attrs={'rows':3,'style' : 'width: 70%'}),
            'Patient_Visit_Investigation_and_Treatment': Textarea(attrs={'rows':3,'style' : 'width: 70%'}),
            'Liver_Examination': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),
            'Spleen_Examination': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),
            'Kidney_Examination': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),
            'Apaankaksha': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),
            'Tongue_Examination': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),
            'Female_Problems': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),
            'Faeces_Examination': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),		
            'Urine_Examination': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),
            'Digestion_Examination': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),
            'Sleep_Problems': Textarea(attrs={'rows':2,'style' : 'width: 70%'}),
			'Med_rec_1': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Med_rec_2': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Med_rec_3': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Med_rec_4': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Med_rec_5': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Med_rec_6': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Med_rec_7': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Med_rec_8': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Med_rec_9': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Med_rec_10': Select(attrs={'rows':2,'style' : 'width: 200px'}),
			'Time_1':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Time_2':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Time_3':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Time_4':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Time_5':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Time_6':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Time_7':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Time_8':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Time_9':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Time_10':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_1':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_2':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_3':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_4':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_5':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_6':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_7':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_8':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_9':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			'Week_10':Select(attrs={'rows':2,'style' : 'width: 100px'}),
			"Billing_Item_1":Select(attrs={'rows':2,'style' : 'width: 265px'}),
			"Billing_Item_2":Select(attrs={'rows':2,'style' : 'width: 265px'}),
			"Billing_Item_3":Select(attrs={'rows':2,'style' : 'width: 265px'}),
			"Billing_Item_4":Select(attrs={'rows':2,'style' : 'width: 265px'}),
			"Billing_Item_5":Select(attrs={'rows':2,'style' : 'width: 265px'}),
			}
	
		



class VisitsRecInline(admin.StackedInline):
		model = VisitsRec
		form = VisitsRecForm
		fieldsets = [
        		(None, {
            'fields': [('Patient_Visit_Date','Patient_Visit_Time'),'Patient_Visit_Complaint','Liver_Examination','Spleen_Examination','Kidney_Examination','Apaankaksha','Tongue_Examination','Female_Problems','Faeces_Examination','Urine_Examination','Digestion_Examination','Sleep_Problems','Patient_Visit_Investigation_and_Treatment',('Med_rec_1', 'Time_1','Week_1'),('Med_rec_2', 'Time_2','Week_2'),('Med_rec_3', 'Time_3','Week_3'),('Med_rec_4', 'Time_4','Week_4'),('Med_rec_5', 'Time_5','Week_5'),('Billing_Item_1','Price_1'),('Billing_Item_2','Price_2'),('Billing_Item_3','Price_3'),('Billing_Item_4','Price_4'),('Billing_Item_5','Price_5'),"Amount_Paid"]
        }),]
		
		extra = 0
		verbose_name = "Visit"
		verbose_name_plural = 'Visits'
		suit_classes = 'suit-tab suit-tab-visits'

class PatientsRecForm(ModelForm):
	
	class Meta:
		model = PatientsRec
		widgets = {
        'Patient_Id' : TextInput(attrs={'size':'20','style' : 'width: 1200px'}),
      			'Address': Textarea(attrs={'rows':2}),
				'Medical_History': Textarea(attrs={'rows':3, 'cols':'20','style' : 'width: 40.9%'}),
				#"photo" : Textarea(attrs={'style' : 'width: 200px','style' : 'height: 240px'}),
	   }
	   
	
class Print_CerificateForm(forms.Form):
	Parent_Name = forms.CharField(max_length=100)
	Treatment = forms.CharField(widget=forms.Textarea)
	Under_Treatment_Since = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
	Under_Treatment_Until = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
	      

class PatientsRecAdmin(admin.ModelAdmin):
		#change_form_template = "random.html"
		list_display = ('Patient_Name', 'Patient_Id', 'Reg_Date','Date_Of_Birth','BloodGroup','Prakruti')
		search_fields = ['Patient_Name','Patient_Id']
		inlines = (VisitsRecInline,)
		class Media:
			#css = {'all':['css/collapsed_stacked_inlines.css']}
			js = ['js/jquery-1.3.2.min.js', 'js/collapsed_stacked_inlines.js',]
		form = PatientsRecForm
		readonly_fields=('Outstanding_Amount','Patient_Id',)
		
		fieldsets = [
        ('Visit', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['Patient_Id',"photo",'Patient_Name','Card_Renewd_On',('Reg_Date','Reg_Time'),'Address',('Contact_No','Email'),'Date_Of_Birth','Birth_Month','Age','Gender','BloodGroup','Prakruti' ,('Referred_By','Occupation'),'Medical_History','Outstanding_Amount']
        }),
		
		('Visit', {
            'classes': ('suit-tab suit-tab-visits',),
            'description': 'Review/Add details of new Patient Encounter',
            'fields': []}),
			
        ]
		
			
		suit_form_tabs = (('general', 'General'),('visits', 'Visits'),)
				 
				
		def save_model(self, request, obj, form, change):
			print str(obj.Patient_Name)
			passeddays = datetime.date.today() - obj.Card_Renewd_On
			if(passeddays.days > 90):
				self.message_user(request, "Attention : Consider Renewing Patient's Card : After renewal of Card, update the ""Renewed On"" field with current date", level=messages.ERROR)
			
			obj.save()
			
class MedicineRecAdmin(admin.ModelAdmin):
    search_fields = ['name_Of_Medicine','price_Of_Medicine']


	   
class FinancialRecordAdmin(admin.ModelAdmin):
		search_fields = ['Description']
		list_display = ('Description','Entry_Type','Date')
		

		

class PrintYourFinancesAdmin(admin.ModelAdmin):
		# def has_add_permission(self, request):
			# return False
		fieldsets = (
			(None, {
				'fields': (('FromYear', 'FromMonth'),('TillYear', 'TillMonth'))
			}),
			)
		    
    



admin.site.register(PatientsRec,PatientsRecAdmin)
admin.site.register(MedicineRec,MedicineRecAdmin)
admin.site.register(TimingsRec)
admin.site.register(FinancialRecord,FinancialRecordAdmin)
admin.site.register(BillingsRec)



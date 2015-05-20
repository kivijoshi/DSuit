from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime   
import pickle
import base64
from django.contrib.auth.models import User
from webcam.fields import CameraField
import random
from webcam.tests import temp_storage



class PatientsRec(models.Model):
	photo = CameraField('CameraPictureField', format='jpeg', null=True, blank=True, upload_to='pictures')
	Gender_Dropdown = (
	('M', 'M'),
	('F', 'F'),)
	BloodGroup_Dropdown = (
	('A+', 'A+'),
	('B+', 'B+'),
	('AB+', 'AB+'),
	('A-', 'A-'),
	('B-', 'B-'),
	('AB-', 'AB-'),
	('O+', 'O+'),
	('O-', 'O-'))
	Prakruti_Dropdown = (
	('Amla', 'Amla'),
	('kshar', 'kshar'),
	('sandha', 'sandha'),
	('Ubhay', 'Ubhay'),)
	Month_Dropdown = (
	('Jan', 'Jan'),('Feb', 'Feb'),('Mar', 'Mar'),('Apr', 'Apr'),('May', 'May'),('Jun', 'Jun'),('Jul', 'Jul'),('Aug', 'Aug'),('Sep', 'Sep'),('Oct', 'Oct'),('Nov', 'Nov'),('Dec', 'Dec'))
	Reg_Date = models.DateField('Registration date')
	Reg_Time = models.TimeField('Registration Time')
	Card_Renewd_On = models.DateField('Card Renewed on',default=datetime.now)
	Patient_Name = models.CharField(max_length = 200)
	Address = models.TextField()
	Date_Of_Birth = models.DateField('Date of birth',blank=True,null=True)
	Gender = models.CharField(max_length=1, choices=Gender_Dropdown)
	Contact_No = models.CharField(max_length = 11,blank=True)
	Email = models.EmailField(max_length = 75,blank = True,verbose_name="Email     :")
	BloodGroup = models.CharField(max_length=3, choices=BloodGroup_Dropdown,blank=True)
	Referred_By = models.CharField(max_length = 100,blank=True)
	Medical_History = models.TextField(blank=True)
	Prakruti = models.CharField(max_length=7, choices=Prakruti_Dropdown,blank=True)
	Occupation = models.CharField(max_length = 50,blank=True,verbose_name="Occupation:")
	Age = models.IntegerField(max_length=3,blank=True,null=True)
	Patient_Id = models.IntegerField(max_length=9,blank=True,null=True)
	Birth_Month = models.CharField(max_length=4, choices=Month_Dropdown)

	def save(self, *args, **kwargs):
	    if not self.pk:
	        self.Patient_Id = len(PatientsRec.objects.all()) + 14111
	    super(PatientsRec, self).save(*args, **kwargs)

	def _get_total1(self):
		Total_f = 0
		Rec_List = VisitsRec.objects.filter(patient_rec = self.id)
		for Rec in Rec_List:
			print Rec
			Total_f = Total_f + (Rec.total - Rec.Amount_Paid)
		return Total_f


	Outstanding_Amount = property(_get_total1)
	def __unicode__(self):
			return self.Patient_Name


class MedicineRec(models.Model):
	name_Of_Medicine = models.CharField(max_length = 100)
	def __unicode__(self):
			return self.name_Of_Medicine

class BillingsRec(models.Model):
	Medicin_Or_Treatments = models.CharField(max_length = 100)
	def __unicode__(self):
			return self.Medicin_Or_Treatments

class TimingsRec(models.Model):
	Time = models.CharField(max_length = 20)
	def __unicode__(self):
			return self.Time


class VisitsRec(models.Model):
	Weeks = (
    ('1', '1'),
    ('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),)
	patient_rec = models.ForeignKey(PatientsRec)
	Med_rec_1 = models.ForeignKey(MedicineRec,related_name="Med_rec_1",blank=True,null=True)
	Time_1 = models.ForeignKey(TimingsRec,related_name="Time_1",blank=True,null=True)
	Week_1 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Med_rec_2 = models.ForeignKey(MedicineRec,related_name="Med_rec_2",blank=True,null=True)
	Time_2 = models.ForeignKey(TimingsRec,related_name="Time_2",blank=True,null=True)
	Week_2 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Med_rec_3 = models.ForeignKey(MedicineRec,related_name="Med_rec_3",blank=True,null=True)
	Time_3 = models.ForeignKey(TimingsRec,related_name="Time_3",blank=True,null=True)
	Week_3 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Med_rec_4 = models.ForeignKey(MedicineRec,related_name="Med_rec_4",blank=True,null=True)
	Time_4 = models.ForeignKey(TimingsRec,related_name="Time_4",blank=True,null=True)
	Week_4 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Med_rec_5 = models.ForeignKey(MedicineRec,related_name="Med_rec_5",blank=True,null=True)
	Time_5 = models.ForeignKey(TimingsRec,related_name="Time_5",blank=True,null=True)
	Week_5 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Med_rec_6 = models.ForeignKey(MedicineRec,related_name="Med_rec_6",blank=True,null=True)
	Time_6 = models.ForeignKey(TimingsRec,related_name="Time_6",blank=True,null=True)
	Week_6 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Med_rec_7 = models.ForeignKey(MedicineRec,related_name="Med_rec_7",blank=True,null=True)
	Time_7 = models.ForeignKey(TimingsRec,related_name="Time_7",blank=True,null=True)
	Week_7 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Med_rec_8 = models.ForeignKey(MedicineRec,related_name="Med_rec_8",blank=True,null=True)
	Time_8 = models.ForeignKey(TimingsRec,related_name="Time_8",blank=True,null=True)
	Week_8 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Med_rec_9 = models.ForeignKey(MedicineRec,related_name="Med_rec_9",blank=True,null=True)
	Time_9 = models.ForeignKey(TimingsRec,related_name="Time_9",blank=True,null=True)
	Week_9 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Med_rec_10 = models.ForeignKey(MedicineRec,related_name="Med_rec_10",blank=True,null=True)
	Time_10 = models.ForeignKey(TimingsRec,related_name="Time_10",blank=True,null=True)
	Week_10 = models.CharField(max_length=2, choices=Weeks,blank=True)
	Patient_Visit_Date = models.DateField('Visit Date')
	Patient_Visit_Time = models.TimeField('Visit Time')
	#Patient_Visit_No = models.AutoField(primary_key=True)
	Patient_Visit_Complaint = models.CharField(max_length = 300,blank=True)
	Patient_Visit_Investigation_and_Treatment = models.CharField(max_length = 300,blank=True)
	Liver_Examination = models.CharField(max_length = 200,blank=True)
	Spleen_Examination = models.CharField(max_length = 200,blank=True)
	Kidney_Examination = models.CharField(max_length = 200,blank=True)
	Apaankaksha = models.CharField(max_length = 200,blank=True)
	Tongue_Examination = models.CharField(max_length = 200,blank=True)
	Female_Problems = models.CharField("Female History",max_length = 200,blank=True)
	Faeces_Examination = models.CharField(max_length = 200,blank=True)
	Urine_Examination = models.CharField(max_length = 200,blank=True)
	Digestion_Examination = models.CharField(max_length = 200,blank=True)
	Sleep_Problems = models.CharField(max_length = 200,blank=True)
	Billing_Item_1 = models.ForeignKey(BillingsRec,related_name="Billing_Item_1",blank=True,null=True)
	Price_1 = models.FloatField(default=0)
	Billing_Item_2 = models.ForeignKey(BillingsRec,related_name="Billing_Item_2",blank=True,null=True)
	Price_2 = models.FloatField(default=0)
	Billing_Item_3 = models.ForeignKey(BillingsRec,related_name="Billing_Item_3",blank=True,null=True)
	Price_3 = models.FloatField(default=0)
	Billing_Item_4 = models.ForeignKey(BillingsRec,related_name="Billing_Item_4",blank=True,null=True)
	Price_4 = models.FloatField(default=0)
	Billing_Item_5 = models.ForeignKey(BillingsRec,related_name="Billing_Item_5",blank=True,null=True)
	Price_5 = models.FloatField(default=0)
	Amount_Paid = models.FloatField(default=0)
	def _get_total(self):

		Total_f = self.Price_1 + self.Price_2 + self.Price_3 + self.Price_4 + self.Price_5


		return Total_f
	total = property(_get_total)
	def __unicode__(self):
			return (str(self.Patient_Visit_Date))[:10]

class FinancialRecord(models.Model):
	IoE = (
	('Income', 'Income'),
	('Expenditure', 'Expenditure'),)

	Entry_Type = models.CharField(max_length = 20,choices=IoE)
	Description = models.CharField(max_length = 100)
	Amount = models.FloatField()
	Date = models.DateField('Date',default=datetime.now())
	def __unicode__(self):
			return self.Description



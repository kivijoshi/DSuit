from django.http import HttpResponse
import time
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER,TA_RIGHT,TA_LEFT
from reportlab.lib.pagesizes import letter,A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from django.contrib import admin
from DoctorsCompanion.models import PatientsRec,VisitsRec,MedicineRec,FinancialRecord,TimingsRec,BillingsRec
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from datetime import datetime
from django.db import models
from  StringIO import StringIO
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from DoctorsCompanion.admin import Print_CerificateForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
#def Prec(request, patient_id):
    #return HttpResponse("Hello, world. You're at the polls index.")

def Prec(request, patient_id):
	
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
	obj = (PatientsRec.objects.get(id = patient_id))
	# Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)
	OPDName = "Mauli Ayurvedalay"
	DoctorsName = "Dr.Hrishikesh Kulkarni"
	Address = "100 feet road, Vishrambag, Sangli 416415"
	Email = "hrk@gmail.com"
	PhoneandMobile = "02332304021/9960326685"
	
	width, height = A4
	height = height-30
	p.setFont("Helvetica", 10, leading = None)
	p.drawCentredString((width/2),(height),"!!Shree!!")
	height = height-30
	p.setFont("Helvetica", 20, leading = None)
	p.drawCentredString((width/2),(height),OPDName)
	height = height-20
	p.setFont("Helvetica", 12, leading = None)
	p.drawCentredString((width/2),(height),Address)
	height = height-20
	p.drawCentredString((width/2),(height),Email)
	height = height-20
	p.drawCentredString((width/2),(height),PhoneandMobile)
	
	height = height-40
	p.setFont("Helvetica", 18, leading = None)
	p.drawCentredString((width/2),(height),"INVOICE")
	
	height = height-40
	p.setFont("Helvetica", 12, leading = None)
	p.drawString((width-150),(height),"Date")
	height = height-20
	p.setFont("Helvetica", 12, leading = None)
	p.drawString((width-150),(height),"Invoice")
	
	height = height-40
	p.setFont("Helvetica", 12, leading = None)
	p.drawString((width-550),(height),"Name of the patient :")
	p.drawString((width-425),(height),obj.Patient_Name)
	height = height-20
	p.setFont("Helvetica", 12, leading = None)
	p.drawString((width-550),(height),"Address :")
	p.drawString((width-425),(height),obj.Address)
	height = height-20
	p.setFont("Helvetica", 12, leading = None)
	p.drawString((width-550),(height),"DOB :")
	p.drawString((width-425),(height),str(obj.Date_Of_Birth))
	height = height-20
	p.setFont("Helvetica", 12, leading = None)
	p.drawString((width-550),(height),"Registration Number :")
	p.drawString((width-425),(height),str(obj.id))
	
	height = height-40
	p.line((width-550),(height),(width-50),(height))
	height = height-20
	p.drawString((width-550),(height), "Treatment/Medicine")
	p.drawString((width-150),(height), "Amount")
	height = height-20
	A = []
	Total = 0
	
	
	Vis_Obj_new = VisitsRec.objects.filter(patient_rec__id=obj.id)
	Vis_Obj = Vis_Obj_new.order_by('-id')[0]
	

	if(Vis_Obj.Billing_Item_1 != None):
		height = height-20
		A = Vis_Obj.Billing_Item_1.Medicin_Or_Treatments
		C = float(Vis_Obj.Price_1)
		Total = Total + C
		D = str(C)
		p.drawString((width-550),(height), A)
		p.drawString((width-150),(height), D)
		
	if(Vis_Obj.Billing_Item_2 != None):
		height = height-20
		A = Vis_Obj.Billing_Item_2.Medicin_Or_Treatments
		C = float(Vis_Obj.Price_2)
		Total = Total + C
		D = str(C)
		p.drawString((width-550),(height), A)
		p.drawString((width-150),(height), D)

	if(Vis_Obj.Billing_Item_3 != None):
		height = height-20
		A = Vis_Obj.Billing_Item_3.Medicin_Or_Treatments
		C = float(Vis_Obj.Price_3)
		Total = Total + C
		D = str(C)
		p.drawString((width-550),(height), A)
		p.drawString((width-150),(height), D)
	
	if(Vis_Obj.Billing_Item_4 != None):
		height = height-20
		A = Vis_Obj.Billing_Item_4.Medicin_Or_Treatments
		C = float(Vis_Obj.Price_4)
		Total = Total + C
		D = str(C)
		p.drawString((width-550),(height), A)
		p.drawString((width-150),(height), D)
	
	if(Vis_Obj.Billing_Item_5 != None):
		height = height-20
		A = Vis_Obj.Billing_Item_5.Medicin_Or_Treatments
		C = float(Vis_Obj.Price_5)
		Total = Total + C
		D = str(C)
		p.drawString((width-550),(height), A)
		p.drawString((width-150),(height), D)
	
	height = height-20
	A = "Previous Outstanding Amount"
	C = obj.Outstanding_Amount - Total
	Total = Total + C
	D = str(C)
	p.drawString((width-550),(height), A)
	p.drawString((width-150),(height), D)
	
	height = height-10
	p.line((width-550),(height),(width-50),(height))
	height = height-20
	p.setFont("Helvetica", 14, leading = None)
	p.drawString((width-350),(height),"Total Amount")
	p.drawString((width-150),(height),str(Total))
	
	height = height-100
	p.line((width-250),(height),(width-50),(height))
	height = height-20
	p.setFont("Helvetica", 12, leading = None)
	p.drawString((width-200),(height),DoctorsName)
	
	
	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response
	
def Print_Certificate(request,patient_id):
        if request.method == 'POST':
            form = Print_CerificateForm(request.POST)
            if form.is_valid():
                ParentName = form.cleaned_data['Parent_Name']
                Treatment = form.cleaned_data['Treatment']
                From = form.cleaned_data['Under_Treatment_Since']
                To = form.cleaned_data['Under_Treatment_Until']
                #HttpResponseRedirect("/thanks/")
                return GenerateCertificate(request,patient_id,ParentName,Treatment,From,To)
            
        form = Print_CerificateForm()
        return render(request, 'printCertificate.html', {'form': form,"ptid":patient_id} )
        
        
def GenerateCertificate(request,patient_id,ParentName,Treatment,From,To):
	try:
		PtObj = (PatientsRec.objects.get(id = patient_id))
	except:
		return messages.error(request, "Wrong Patient Registration Id : Please correct ID then press save and continue editing. After that print the certificate")
	PatientName =  PtObj.Patient_Name
	print PatientName
	PatientGender = PtObj.Gender
	

	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
	
	buff = StringIO()
	pdf = SimpleDocTemplate(buff, pagesize = A4, rightMargin=70, leftMargin=70, topMargin=50,bottomMargin=70)
	story = []
	style = getSampleStyleSheet()
	Head1 = style["Normal"]
	Head1.fontName = "Helvetica"
	Head1.spaceBefore = 10
	Head1.spaceAfter = 2
	Head1.leading = 30
	Head1.fontSize = 20
	Head1.alignment = TA_CENTER
	text = "Mauli Ayurvedalay"
	para = Paragraph(text, Head1)
	story.append(para)
	story.append(Spacer(1, 1))
	
	style = getSampleStyleSheet()
	Head2 = style["Normal"]
	Head2.fontName = "Helvetica"
	Head2.spaceBefore = 10
	Head2.spaceAfter = 10
	Head2.leading = 15
	Head2.fontSize = 12
	Head2.alignment = TA_CENTER
	text = "Dr.Hrishikesh Kulkarni<br/>100 feet road, Vishrambag, Sangli 416415<br/>hrk@gmail.com<br/>02332304021/9960326685"
	para = Paragraph(text, Head2)
	story.append(para)
	story.append(Spacer(1, 60))
	
	style = getSampleStyleSheet()
	normal = style["Normal"]
	normal.fontName = "Helvetica"
	normal.leading = 15
	normal.fontSize = 30
	normal.alignment = TA_CENTER
	text = "MEDICAL CERTIFICATE"
	para = Paragraph(text, normal)
	story.append(para)
	story.append(Spacer(1, 60))
	
	style = getSampleStyleSheet()
	lefty = style["Normal"]
	lefty.fontName = "Helvetica"
	lefty.spaceBefore = 10
	lefty.spaceAfter = 10
	lefty.leading = 30
	lefty.fontSize = 12
	lefty.alignment = TA_JUSTIFY
	
	if(PatientGender == "M"):
		if(str(ParentName) != ""):
			ParentLine = "; Son of " + str(ParentName)
		else:
			ParentLine = ""
		text = '    This is to certify that Mr. %s%s is under my treatment for Flue from %s to %s. <br/>    He is/was advised complete rest for period. He is medically fit to resume from %s.'% (PatientName,ParentLine,From,To,To) 
	else:
		if(str(ParentName) != ""):
			ParentLine = "; Daughter of " + str(ParentName)
		else:
			ParentLine = ""
		text = "    This is to certify that Ms. %s%s is under my treatment for Flue from %s to %s. <br/>    She is/was advised complete rest for period. She is medically fit to resume from %s."% (PatientName,ParentLine,From,To,To)  
	para = Paragraph(text, lefty)
	story.append(para)
	story.append(Spacer(1, 100))
	
	
	style = getSampleStyleSheet()
	righty = style["Normal"]
	righty.fontName = "Helvetica"
	righty.spaceBefore = 10
	righty.spaceAfter = 10
	righty.leading = 30
	righty.fontSize = 12
	righty.alignment = TA_RIGHT
	text = "-------------------------------------"
	para = Paragraph(text, righty)
	story.append(para)
	text = "Stamp and Signature"
	para = Paragraph(text, righty)
	story.append(para)
	
	pdf.build(story)
	
	
	response.write(buff.getvalue())
	buff.close()
	return response
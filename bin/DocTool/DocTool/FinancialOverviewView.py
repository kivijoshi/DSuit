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
from django.shortcuts import render
from django.http import HttpResponseRedirect
from DoctorsCompanion.Finance import FinancialOverviewForm

def FinancialOverview(request):
        if request.method == 'POST':
            form = FinancialOverviewForm(request.POST)
            if form.is_valid():
                From = form.cleaned_data['Overview_From']
                To = form.cleaned_data['Overview_Until']
                return GenerateFinancialOverview(request,From,To)
            
        form = FinancialOverviewForm()
        return render(request, 'FinancialOverview.html', {'form': form} )
      
     
def GenerateFinancialOverview(request,From,To):
	
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
	
	# Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)
	
	
	Debit_Credit_List = GenerateBalanceSheet(From,To)
	
	Debit_Credit_List.sort(key=lambda x: x[0])

	width, height = A4
	height = height-30
	header = "Mauli Ayurvedalaya Financial Transactions From " + str(From) + " To " + str(To)
	p.drawString((width-550),(height), header)
	height = height-10
	p.line((width-550),(height),(width-50),(height))
	height = height-60
	p.drawString((width-550),(height), "Date")
	p.drawString((width-450),(height), "Credit Entry")
	p.drawString((width-350),(height), "Debit Entry")
	p.drawString((width-250),(height), "Description")
	
	Credit = 0
	Debit = 0
	for Fin_rec in Debit_Credit_List:
		height = height-30
		p.drawString((width-550),(height), (str(Fin_rec[0]))[:10])
		if(Fin_rec[1] == 'C'):
			p.drawString((width-450),(height), str(Fin_rec[2]))
			Credit = Credit + Fin_rec[2]
		if(Fin_rec[1] == 'D'):
			p.drawString((width-350),(height), str(Fin_rec[2]))
			Debit = Debit + Fin_rec[2]
		p.drawString((width-250),(height), str(Fin_rec[3]))
		if(height<=70):
			p.showPage()
			width, height = A4
			height = height-30
			header = "Mauli Ayurvedalaya Financial Transactions From " + str(From) + " To " + str(To)
			p.drawString((width-550),(height), header)
			height = height-10
			p.line((width-550),(height),(width-50),(height))
			height = height-60
			p.drawString((width-550),(height), "Date")
			p.drawString((width-450),(height), "Credit Entry")
			p.drawString((width-350),(height), "Debit Entry")
			p.drawString((width-250),(height), "Description")
			
	
	# Close the PDF object cleanly, and we're done.
	p.showPage()
	width, height = A4
	height = height-30
	header = "Mauli Ayurvedalaya Financial Transactions From " + str(From) + " To " + str(To)
	p.drawString((width-550),(height), header)
	height = height-10
	p.line((width-550),(height),(width-50),(height))
	height = height-60
	p.setFont("Helvetica", 20, leading = None)
	p.drawCentredString((width/2),(height),"Final Consolidation")
	height = height-30
	p.setFont("Helvetica", 15, leading = None)
	p.drawString((width-550),(height), "Total Credit = ")
	p.drawString((width-350),(height), str(Credit))
	height = height-20
	p.drawString((width-550),(height), "Total Debit  = ")
	p.drawString((width-350),(height), str(Debit))
	height = height-20
	p.line((width-550),(height),(width-50),(height))
	height = height-20
	p.drawString((width-550),(height), "Total = ")
	p.drawString((width-350),(height), str(Credit - Debit))
	p.save()
	return response
 
def GenerateBalanceSheet( startdate,enddate ):

	Debit_Credit_List = []
	
	VisitRecordList = VisitsRec.objects.all()
	for VisRecord in VisitRecordList:
		if(startdate <= VisRecord.Patient_Visit_Date and enddate>= VisRecord.Patient_Visit_Date):
			Debit_Credit_List.append([VisRecord.Patient_Visit_Date,'C',VisRecord.total,VisRecord.patient_rec.Patient_Name])
	
	
	FinancialRecordList = FinancialRecord.objects.all()
	for FinancialRec in FinancialRecordList:
		if(startdate <= FinancialRec.Date and enddate>= FinancialRec.Date):
			if(FinancialRec.Entry_Type == 'Income'):
				Debit_Credit_List.append([FinancialRec.Date,'C',FinancialRec.Amount,FinancialRec.Description])
			if(FinancialRec.Entry_Type == 'Expenditure'):
				Debit_Credit_List.append([FinancialRec.Date,'D',FinancialRec.Amount,FinancialRec.Description])
	

  
	return Debit_Credit_List
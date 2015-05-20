from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views,FinancialOverviewView
from django.contrib.admin import site, ModelAdmin





urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DocTool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/DoctorsCompanion/patientsrec/(?P<patient_id>\d+)/print/$', views.Prec, name='Prec'),
	url(r'^admin/DoctorsCompanion/patientsrec/(?P<patient_id>\d+)/printMedicalCertificate/$', views.Print_Certificate, name='Print_Certificate'),
   url(r'^FinancialOverview/$', FinancialOverviewView.FinancialOverview, name='FinancialOverview'),
    url(r'^admin/', include(admin.site.urls)),
                 
)

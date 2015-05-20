# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingsRec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Medicin_Or_Treatments', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FinancialRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Entry_Type', models.CharField(max_length=20, choices=[(b'Income', b'Income'), (b'Expenditure', b'Expenditure')])),
                ('Description', models.CharField(max_length=100)),
                ('Amount', models.FloatField()),
                ('Entry_Date_1', models.DateTimeField(verbose_name=b'Entry Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedicineRec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_Of_Medicine', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatientsRec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Reg_Date', models.DateTimeField(verbose_name=b'Registration date')),
                ('Card_Renewd_On', models.DateField(default=datetime.datetime.now, verbose_name=b'Card Renewed on')),
                ('Patient_Name', models.CharField(max_length=200)),
                ('Address', models.TextField()),
                ('Date_Of_Birth', models.DateField(null=True, verbose_name=b'Date of birth', blank=True)),
                ('Gender', models.CharField(max_length=1, choices=[(b'M', b'M'), (b'F', b'F')])),
                ('Contact_No', models.CharField(max_length=11, blank=True)),
                ('Email', models.EmailField(max_length=75, blank=True)),
                ('BloodGroup', models.CharField(blank=True, max_length=3, choices=[(b'A+', b'A+'), (b'B+', b'B+'), (b'AB+', b'AB+'), (b'A-', b'A-'), (b'B-', b'B-'), (b'AB-', b'AB-'), (b'O+', b'O+'), (b'O-', b'O-')])),
                ('Referred_By', models.CharField(max_length=100, blank=True)),
                ('Medical_History', models.TextField(blank=True)),
                ('Prakruti', models.CharField(blank=True, max_length=7, choices=[(b'Amla', b'Amla'), (b'kshar', b'kshar'), (b'sandha', b'sandha'), (b'Ubhay', b'Ubhay')])),
                ('Occupation', models.CharField(max_length=50, blank=True)),
                ('Age', models.IntegerField(max_length=3, null=True, blank=True)),
                ('Patient_Id', models.IntegerField(max_length=9, null=True, blank=True)),
                ('Birth_Month', models.CharField(max_length=4, choices=[(b'Jan', b'Jan'), (b'Feb', b'Feb'), (b'Mar', b'Mar'), (b'Apr', b'Apr'), (b'May', b'May'), (b'Jun', b'Jun'), (b'Jul', b'Jul'), (b'Aug', b'Aug'), (b'Sep', b'Sep'), (b'Oct', b'Oct'), (b'Nov', b'Nov'), (b'Dec', b'Dec')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Print_Cerificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Patient_Id', models.IntegerField(max_length=6)),
                ('Son_Or_Daughter_Of', models.CharField(max_length=100, blank=True)),
                ('Under_Treatment_For', models.CharField(max_length=100, blank=True)),
                ('FromDate', models.DateField(verbose_name=b'From')),
                ('ToDate', models.DateField(verbose_name=b'To')),
                ('Resume_From', models.DateField(verbose_name=b'Resume From')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PrintYourFinances',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FromYear', models.IntegerField(blank=True, max_length=4, null=True, choices=[(2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098), (2099, 2099), (2100, 2100), (2101, 2101), (2102, 2102), (2103, 2103), (2104, 2104), (2105, 2105), (2106, 2106), (2107, 2107), (2108, 2108), (2109, 2109), (2110, 2110), (2111, 2111), (2112, 2112), (2113, 2113)])),
                ('FromMonth', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('TillYear', models.IntegerField(blank=True, max_length=4, null=True, choices=[(2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098), (2099, 2099), (2100, 2100), (2101, 2101), (2102, 2102), (2103, 2103), (2104, 2104), (2105, 2105), (2106, 2106), (2107, 2107), (2108, 2108), (2109, 2109), (2110, 2110), (2111, 2111), (2112, 2112), (2113, 2113)])),
                ('TillMonth', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimingsRec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Time', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VisitsRec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Week_1', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Week_2', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Week_3', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Week_4', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Week_5', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Week_6', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Week_7', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Week_8', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Week_9', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Week_10', models.CharField(blank=True, max_length=2, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10')])),
                ('Patient_Visit_Date', models.DateTimeField(verbose_name=b'Patient visit date')),
                ('Patient_Visit_Complaint', models.CharField(max_length=300, blank=True)),
                ('Patient_Visit_Investigation_and_Treatment', models.CharField(max_length=300, blank=True)),
                ('Liver_Examination', models.CharField(max_length=200, blank=True)),
                ('Spleen_Examination', models.CharField(max_length=200, blank=True)),
                ('Kidney_Examination', models.CharField(max_length=200, blank=True)),
                ('Apaankaksha', models.CharField(max_length=200, blank=True)),
                ('Tongue_Examination', models.CharField(max_length=200, blank=True)),
                ('Female_Problems', models.CharField(max_length=200, verbose_name=b'Female History', blank=True)),
                ('Faeces_Examination', models.CharField(max_length=200, blank=True)),
                ('Urine_Examination', models.CharField(max_length=200, blank=True)),
                ('Digestion_Examination', models.CharField(max_length=200, blank=True)),
                ('Sleep_Problems', models.CharField(max_length=200, blank=True)),
                ('Price_1', models.FloatField(default=0)),
                ('Price_2', models.FloatField(default=0)),
                ('Price_3', models.FloatField(default=0)),
                ('Price_4', models.FloatField(default=0)),
                ('Price_5', models.FloatField(default=0)),
                ('Amount_Paid', models.FloatField(default=0)),
                ('Billing_Item_1', models.ForeignKey(related_name='Billing_Item_1', blank=True, to='DoctorsCompanion.BillingsRec', null=True)),
                ('Billing_Item_2', models.ForeignKey(related_name='Billing_Item_2', blank=True, to='DoctorsCompanion.BillingsRec', null=True)),
                ('Billing_Item_3', models.ForeignKey(related_name='Billing_Item_3', blank=True, to='DoctorsCompanion.BillingsRec', null=True)),
                ('Billing_Item_4', models.ForeignKey(related_name='Billing_Item_4', blank=True, to='DoctorsCompanion.BillingsRec', null=True)),
                ('Billing_Item_5', models.ForeignKey(related_name='Billing_Item_5', blank=True, to='DoctorsCompanion.BillingsRec', null=True)),
                ('Med_rec_1', models.ForeignKey(related_name='Med_rec_1', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Med_rec_10', models.ForeignKey(related_name='Med_rec_10', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Med_rec_2', models.ForeignKey(related_name='Med_rec_2', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Med_rec_3', models.ForeignKey(related_name='Med_rec_3', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Med_rec_4', models.ForeignKey(related_name='Med_rec_4', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Med_rec_5', models.ForeignKey(related_name='Med_rec_5', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Med_rec_6', models.ForeignKey(related_name='Med_rec_6', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Med_rec_7', models.ForeignKey(related_name='Med_rec_7', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Med_rec_8', models.ForeignKey(related_name='Med_rec_8', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Med_rec_9', models.ForeignKey(related_name='Med_rec_9', blank=True, to='DoctorsCompanion.MedicineRec', null=True)),
                ('Time_1', models.ForeignKey(related_name='Time_1', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('Time_10', models.ForeignKey(related_name='Time_10', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('Time_2', models.ForeignKey(related_name='Time_2', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('Time_3', models.ForeignKey(related_name='Time_3', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('Time_4', models.ForeignKey(related_name='Time_4', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('Time_5', models.ForeignKey(related_name='Time_5', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('Time_6', models.ForeignKey(related_name='Time_6', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('Time_7', models.ForeignKey(related_name='Time_7', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('Time_8', models.ForeignKey(related_name='Time_8', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('Time_9', models.ForeignKey(related_name='Time_9', blank=True, to='DoctorsCompanion.TimingsRec', null=True)),
                ('patient_rec', models.ForeignKey(to='DoctorsCompanion.PatientsRec')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

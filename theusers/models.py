from django.db import models
import datetime

# Create your models here.
Designation = (
    ('DGP & SPC', 'Director General of Police & State Police Chief (DGP & SPC)'),
    ('ADGP', 'Additional Director General of Police (ADGP)'),
    ('IG', 'Inspector General of Police (IG)'),
    ('DIG', 'Deputy Inspector General of Police (DIG)'),
    ('SP (Selection Grade)', 'Superintendent of Police (Selection Grade) (SP(SG))'),
    ('SP', 'Superintendent of Police (SP)'),
    ('Addl.SP', 'Additional Superintendent of Police (Addl.SP)'),
    ('ASP', 'Assistant Superintendent of Police (ASP) [IPS]'),
    ('ASP(Probationary Rank: 2 years of service)', 'Assistant Superintendent of Police (Probationary Rank: 2 years of service)(ASP) [IPS Trainee]'),
    ('ASP(Probationary Rank: 1 year of service)', 'Assistant Superintendent of Police (Probationary Rank: 1 year of service)(ASP) [IPS Trainee]'),
    ('DYSP', 'Deputy Superintendent of Police (DYSP) [KPS]'),
    ('IP', 'Inspector of Police (IP)'),
    ('SI', 'Sub-Inspector of Police (SI)'),
    ('ASI', 'Assistant Sub-Inspector of Police (ASI)'),
    ('SCPO', 'Head constable/Senior Civil Police Officer (SCPO)'),
    ('CPO', 'Constable/Civil Police Officer (CPO)')
)

District = (
    ('Thiruvananthapuram','Thiruvananthapuram'),
    ('Kollam','Kollam'),
    ('Pathanamthitta','Pathanamthitta'),
    ('Alappuzha','Alappuzha'),
    ('Kottayam','Kottayam'),
    ('Idukki','Idukki'),
    ('Ernakulam', 'Ernakulam'),
    ('Thrissur','Thrissur'),
    ('Palakkad','Palakkad'),
    ('Malappuram','Malappuram'),
    ('Kozhikode','Kozhikode'),
    ('Wayanad', 'Wayanad'),
    ('Kannur','Kannur'),
    ('Kasaragod','Kasaragod'),
)
GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female')
)


class Policestation(models.Model):
    stationid=models.IntegerField(primary_key=True)
    stationname=models.CharField(max_length=200)  
    addr1=models.CharField(max_length=200)  
    addr2=models.CharField(max_length=200) 
    district = models.CharField(max_length=25, choices=District, default='') 
    city = models.CharField(max_length=200)  
    contact_no = models.CharField(max_length=10)                                       
    email=models.EmailField()
    password=models.CharField(max_length=100)
    approve=models.IntegerField(default=0)
    usertype=models.CharField(max_length=25,default='station')
    def __str__(self):
        return self.stationname

class Stationstaff(models.Model):
    stationid=models.ForeignKey(Policestation,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100) 
    addr=models.TextField()  
    gender = models.CharField(max_length=25,choices=GENDER_CHOICES) 
    dob = models.DateField(("D.O.B"), default=datetime.date.today) 
    designation=models.CharField(max_length=100,choices=Designation)
    policestation=models.CharField(max_length=100) 
    contact_no = models.CharField(max_length=10)                    
    email=models.EmailField()
    password=models.CharField(max_length=100)
    approve=models.IntegerField(default=0)
    usertype=models.CharField(max_length=25,default='staff')
    work_history=models.FileField(upload_to='work_history/',null=True) 
    

class Publicuser(models.Model):
    name=models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)                         
    email=models.EmailField()
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=25,default='public')


class LoginForm(models.Model):                         
    email=models.EmailField()
    password=models.CharField(max_length=100)
    
class Criminal(models.Model):
    name=models.CharField(max_length=100)
    gender = models.CharField(max_length=25,choices=GENDER_CHOICES) 
    crimedetails=models.TextField()  
    image=models.FileField(upload_to='images/') 
    stationid=models.ForeignKey(Policestation,on_delete=models.CASCADE,null=True)                         
    currentdate = models.DateField(auto_now_add=True) 

class Staffduty(models.Model):
    date = models.DateField(("date"), default=datetime.date.today) 
    duty=models.CharField(max_length=5000)
    staffid=models.ForeignKey(Stationstaff,on_delete=models.CASCADE,null=True)
    stationid=models.ForeignKey(Policestation,on_delete=models.CASCADE,null=True)                         
    currentdate = models.DateField(auto_now_add=True)
    
class Case(models.Model):
    petitionername=models.CharField(max_length=100) 
    petitioneraddr=models.TextField()
    petitionercontact_no = models.CharField(max_length=10)                         
    aadharno= models.CharField(max_length=12) 
    case=models.CharField(max_length=5000)
    casedetails=models.TextField()  
    staffid=models.ForeignKey(Stationstaff,on_delete=models.CASCADE,null=True)
    currentdate = models.DateField(auto_now_add=True)
    fir=models.FileField(upload_to='fir/',null=True) 
    

class Publiccase(models.Model):
    aadharno= models.CharField(max_length=12) 
    petitioneraddr=models.TextField()
    case=models.CharField(max_length=5000)
    casedetails=models.TextField()  
    stationid=models.ForeignKey(Policestation,on_delete=models.CASCADE,null=True)
    publicid=models.ForeignKey(Publicuser,on_delete=models.CASCADE,null=True)
    currentdate = models.DateField(auto_now_add=True)
    status=models.TextField(default='Pending')
    fir=models.FileField(upload_to='fir/',null=True) 


class Complaint(models.Model):
    subject=models.CharField(max_length=5000)
    complaint=models.TextField()  
    currentdate = models.DateField(auto_now_add=True)
    publicid=models.ForeignKey(Publicuser,on_delete=models.CASCADE,null=True)
    pcaseid=models.ForeignKey(Publiccase,on_delete=models.CASCADE,null=True)
    reply=models.TextField(default='Pending')

class Attendance(models.Model):
    staffid=models.ForeignKey(Stationstaff,on_delete=models.CASCADE,null=True)
    stationid=models.ForeignKey(Policestation,on_delete=models.CASCADE,null=True)
    attendance=models.CharField(max_length=500,default='Absent')
    date = models.DateField(auto_now_add=True)
                            
class Staffchat(models.Model):
    message=models.TextField()
    senderid=models.ForeignKey(Stationstaff,on_delete=models.CASCADE,null=True)
    recieverid=models.ForeignKey(Publicuser,on_delete=models.CASCADE,null=True)
    date_time = models.DateTimeField(auto_now_add = True)  

class Publicchat(models.Model):
    message=models.TextField()
    senderid=models.ForeignKey(Publicuser,on_delete=models.CASCADE,null=True)
    recieverid=models.ForeignKey(Stationstaff,on_delete=models.CASCADE,null=True)
    date_time = models.DateTimeField(auto_now_add = True)  

class salary(models.Model):
    designation=models.CharField(max_length=100,choices=Designation)
    basic_salary=models.FloatField(default=0) 
    HRA=models.FloatField(default=0) 
    DA=models.FloatField(default=0) 
    PF=models.FloatField(default=0) 
    total_salary=models.FloatField(default=0) 
    
class FIR(models.Model):
    FIR_No = models.AutoField(primary_key=True)
    caseid = models.ForeignKey(Publiccase, on_delete=models.CASCADE, null=True, blank=True, related_name='fir_cases')
    caseid2 = models.ForeignKey(Case, on_delete=models.CASCADE, null=True, blank=True, related_name='fir_cases')
    court = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    PSname = models.CharField(max_length=100)
    date_of_case_given = models.DateField()
    Act = models.CharField(max_length=1000)
    Sections = models.CharField(max_length=100)   
    date_of_crime = models.DateField()
    location = models.TextField()
    Petitioner_name = models.CharField(max_length=100)
    Details_of_known_Suspected = models.TextField()
    Case_description = models.TextField()
    

class Demo(models.Model):
    name= models.CharField(max_length=25)
class Demo1(models.Model):
    name1= models.CharField(max_length=25)

 
 
   
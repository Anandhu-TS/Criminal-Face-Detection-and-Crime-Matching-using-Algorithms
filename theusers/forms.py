from django import forms
from .models import Policestation, Stationstaff, Publicuser,GENDER_CHOICES, LoginForm, Criminal, Staffduty, Case, Publiccase, Complaint
from .models import Staffchat, Publicchat, Designation, salary, FIR
class Station(forms.ModelForm):
    class Meta:
        model = Policestation
        fields = ['stationid','stationname','addr1','addr2','district','city','contact_no','email','password']
        widgets={
            'password': forms.PasswordInput(),
        }

class Staff(forms.ModelForm):
    # gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    station=forms.ModelChoiceField(queryset=Policestation.objects.all(),empty_label="select station")
    class Meta:
        model = Stationstaff
        
        fields = ['name','addr','gender','dob','designation','contact_no','email','password']
        widgets={
            'station':forms.Select(),
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(),
        }

class Public(forms.ModelForm):
    class Meta:
        model = Publicuser
        fields = ['name','contact_no','email','password']
        widgets={
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # class Meta:
    #     model = LoginForm
    #     fields = ['email','password']
    #     widgets={
    #         'password': forms.PasswordInput(),
    #     }
        
class Stationedit(forms.ModelForm):
    class Meta:
        model = Policestation
        fields = ['stationname','addr1','addr2','district','city','contact_no','email']
       
class Staffedit(forms.ModelForm):
    class Meta:
        model = Stationstaff
        fields = ['name','addr','gender','dob','designation','contact_no','email']
        widgets={
            'dob': forms.DateInput(attrs={'type': 'date'}),
            
        }

class Publicedit(forms.ModelForm):
    class Meta:
        model = Publicuser
        fields = ['name','contact_no','email',]
        

class Criminaladd(forms.ModelForm):
    class Meta:
        model = Criminal
        fields = ['name','gender','crimedetails','image']
    
class Dutyadd(forms.ModelForm):
    class Meta:
        model = Staffduty
        fields = ['date','duty']
        widgets={
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class Staffcasereg(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['petitionername','petitioneraddr','petitionercontact_no','aadharno','case','casedetails']

class Caseedit(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['petitionername','petitioneraddr','petitionercontact_no','aadharno','case','casedetails']

class Pcaseedit(forms.ModelForm):
    class Meta:
        model = Publiccase
        fields = ['petitioneraddr','aadharno','case','casedetails']
       
class Publiccasereg(forms.ModelForm):
    station=forms.ModelChoiceField(queryset=Policestation.objects.all(),empty_label="Select a station")
    class Meta:
        model = Publiccase
        fields = ['aadharno','petitioneraddr','case','casedetails']
        widgets={
            'station':forms.Select(),
        }

class Publiccaseedit(forms.ModelForm):
    class Meta:
        model = Publiccase
        fields = ['aadharno','petitioneraddr','case','casedetails']

class Complaintadd(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['subject','complaint']

class Statusadd(forms.ModelForm):
    class Meta:
        model = Publiccase
        fields = ['status']

class Replyadd(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['reply']

class Pfirupload(forms.ModelForm):
    class Meta:
        model = Publiccase
        fields = ['fir']

class Firupload(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['fir']

class Publicstaffchat(forms.ModelForm):
    class Meta:
        model = Publicchat
        fields = ['message']

class Staffpublicchat(forms.ModelForm):
    class Meta:
        model = Staffchat
        fields = ['message']

class Promotion(forms.ModelForm):
    class Meta:
        model = Stationstaff
        fields = ['designation']
        
class Salary(forms.ModelForm):
    class Meta:
        model = salary
        fields = ['designation','basic_salary','HRA','DA','PF']

class Workhistory(forms.ModelForm):
    class Meta:
        model = Stationstaff
        fields = ['work_history']

class FIRForm(forms.ModelForm):
    class Meta:
        model = FIR
        fields = ['court','district','PSname','date_of_case_given','Act','Sections','date_of_crime','location','Petitioner_name','Details_of_known_Suspected','Case_description']
        widgets = {
            'date_of_case_given': forms.DateInput(attrs={'type': 'date'}),
            'date_of_crime': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.Textarea(attrs={'rows': 4}),
            'Case_description': forms.Textarea(attrs={'rows': 4}),
        }

class FirCheckForm(forms.ModelForm):
    class Meta:
        model = FIR
        fields = ['Case_description']
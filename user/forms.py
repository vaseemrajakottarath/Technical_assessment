from django import forms
from .models import User,Department

class RegistrationForms(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'form-control'
    }))
    department=forms.ModelChoiceField(
        queryset=Department.objects.all(),
        initial=0
    )
    
    class Meta: 
        model= User
        fields =['name','phone_number','email','password','role']
    
    def clean(self):
        cleaned_data = super(RegistrationForms,self).clean()
        password =cleaned_data.get('password')
        # confirm_password = cleaned_data.get('confirm_password')


        # if password != confirm_password:
        #     raise forms.ValidationError(
        #         "Password does not match"
        #     )
    

    def __init__(self,*args,**kwargs):
        super(RegistrationForms,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder']='Enter First name'
        # self.fields['last_name'].widget.attrs['placeholder']='Enter Last name'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter phone number'
        self.fields['email'].widget.attrs['placeholder']='Enter email address'
        

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
            
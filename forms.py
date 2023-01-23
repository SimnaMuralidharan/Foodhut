from django import forms
class regform(forms.Form):
    fullname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    gender=forms.CharField(max_length=20)
    password=forms.CharField(max_length=30)
    cpassword=forms.CharField(max_length=30)

class logform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

class nonform(forms.Form):
    nitem=forms.CharField(max_length=25)
    nprice=forms.IntegerField()
    ndes=forms.CharField(max_length=100)
    nimage=forms.FileField()


class vegform(forms.Form):
    vitem = forms.CharField(max_length=25)
    vprice = forms.IntegerField()
    vdes = forms.CharField(max_length=100)
    vimage = forms.FileField()

class adddetails(forms.Form):
    rimage=forms.FileField()
    rid=forms.IntegerField()
    rname=forms.CharField(max_length=25)
    rno=forms.IntegerField()
    rloc=forms.CharField(max_length=50)
    ropen=forms.TimeField()
    rclose=forms.TimeField()
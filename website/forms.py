from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class UpdateFileForm(forms.Form):
    updatefile = forms.FileField(required=False)
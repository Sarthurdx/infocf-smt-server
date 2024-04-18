from django import forms
from django.utils.safestring import mark_safe

class NameForm(forms.Form):
    #your_name = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    ckb= forms.CharField(widget=forms.Textarea(),label=("CKB\n"))
    query= forms.CharField(widget=forms.Textarea(attrs={"rows":1}), label=("Query\n"), required=False)
    parallelize = forms.BooleanField(initial=True, label=("Parallelized Compilation"), required=False)
    cw = forms.BooleanField(initial=False, label=("Compute cw-minima"), required=False)
    res = ""
    minimas = ""

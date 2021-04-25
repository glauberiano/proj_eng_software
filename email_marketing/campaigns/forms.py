from django import forms


class ContentForm(forms.Form):
    campaign = forms.CharField(label='Campanha', max_length=150)
    created_by = forms.CharField(label='Criado por', max_length=100)
    responsible = forms.CharField(label='Responsaveis', max_length=250)
    subject = forms.CharField(label='Assunto', max_length=100)
    
from django import forms


class CardForm(forms.Form):
    card_id = forms.IntegerField(required=True)
    understood = forms.BooleanField(required=False)

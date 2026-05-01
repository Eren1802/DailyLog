from django import forms
from datetime import date, timedelta

class DailyLogForm(forms.Form):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        required=False
    )
    done = forms.CharField(required=True)
    pending = forms.CharField(required=False)
    mood = forms.CharField(required=False)

    def clean_date(self):
        d = self.cleaned_data['date']
        if d < date.today() - timedelta(days=7):
            raise forms.ValidationError("You can only log within the past 7 days.")
        if d > date.today():
            raise forms.ValidationError("You can't log a future date.")
        return d
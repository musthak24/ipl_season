from django import forms

from ipl.models import Match

class SeasonForm(forms.Form):
    season = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(SeasonForm, self).__init__(*args, **kwargs)

        query = Match.objects.all().values_list('season', 'season').distinct().order_by('season')
        query = list(query)
        c = [("", "---------")] + query

        self.fields['season'].choices = c

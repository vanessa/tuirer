from django import forms

from tuites.models import Tuite
from users.models import User


class PostTuiteForm(forms.ModelForm):
    class Meta:
        model = Tuite
        fields = ['content', 'creator']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        creator_id = self.initial['creator']
        self.fields['creator'].initial = User.objects.get(id=creator_id)
        self.fields['creator'].widget = forms.HiddenInput()

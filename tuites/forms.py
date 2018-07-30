from django import forms

from tuites.models import Tuite
from users.models import User


class PostTuiteForm(forms.ModelForm):
    class Meta:
        model = Tuite
        fields = ['content', 'creator']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        creator_id = self.initial.get('creator')
        self.fields['creator'].initial = User.objects.get(id=creator_id)
        # Utilizamos o HiddenInput() porque não queremos que o usuário
        # selecione quem é o criador do Tuite.
        self.fields['creator'].widget = forms.HiddenInput()

    def clean_creator(self):
        creator_chosen = self.cleaned_data.get('creator')
        initial_creator = self.initial.get('creator')
        # Abaixo usamos o id porque o formulrio, quando postado,
        # retornar o objeto do usurio, diferente do parmetro que
        # passamos para iniciar o formulrio, que foi o id
        if creator_chosen.id != initial_creator:
            raise forms.ValidationError(
                'Você está tentando burlar o sistema!',
                code='invalid')
        return creator_chosen

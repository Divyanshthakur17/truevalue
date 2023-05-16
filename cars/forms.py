from django import forms
from .models import Commentcars

class CarCommentForm(forms.ModelForm):
    content = forms.CharField(
        widget = forms.Textarea(
            attrs= {
                'class': 'form-control',
                'id': 'message',
                'cols': '30',
                'rows': '10',
            }
        )
    )

    class Meta:
        model = Commentcars
        fields = ('content',)

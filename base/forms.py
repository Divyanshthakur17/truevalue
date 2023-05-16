from django import forms
from .models import Comment
from accounts.models import User
from image_cropping import ImageCropWidget


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="Comments",widget=forms.Textarea(attrs={
        'rows':'4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_image',)
        widgets = {
            'user_image': ImageCropWidget,
        }
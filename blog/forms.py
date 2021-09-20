from django.forms import ModelForm
from .models import Post



# class BlogFor(forms.Form):
#     name= forms.CharField(label="enter here", max_length=50)
#     tagline = forms.CharField(widget=forms.Textarea)



class PostcreateForm(ModelForm):
    class Meta:
        model = Post
        fields=('__all__')



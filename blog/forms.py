from django import forms
from .models import Comment
from .models import Post
from django.forms import TextInput, Textarea

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25)
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)
class CommentForm(forms.ModelForm):
	name = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Tu nombre','class' : 'myfieldclass'}))
	body = forms.CharField(label="",widget=forms.Textarea(attrs={'placeholder': 'Tu commentario','style': 'width:75%','class' : 'myfieldclass'}))

	class Meta:
		model = Comment
		fields = ('name', 'body')
		



class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'body',)
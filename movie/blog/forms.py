from django import forms

class BlogForm(forms.Form):
	title = forms.CharField(label='Title:', max_length = 50000 )
	blog = forms.CharField(label='Your Blog', max_length=50000)
from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     username = forms.CharField(label="your name", max_length=100, error_messages={
#         'required': 'Please enter your name',
#         'max_length': 'Name is too long'
#     })
#     rating = forms.IntegerField(label="your rating", min_value=1, max_value=5)
#     review_text = forms.CharField(label="your review", widget=forms.Textarea)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
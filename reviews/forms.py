from django import forms

from reviews.models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "max_length": "Please enter a shorter name",
#         "required": "User name must not be empty"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=1000)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['owner_comment']
        labels = {
            'username': "User Name",
            'review_text': "Feedback",
            'rating': "Rating"
        }
        error_messages = {
            "username": {
                'required': "Name must not be empty",
                'max_length': "Name can have maximum 100 letters"
            }
        }


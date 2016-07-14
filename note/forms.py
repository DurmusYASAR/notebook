from django import forms
from .models import Post
from datetimewidget.widgets import DateTimeWidget
from django.db import models

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('end_time', 'title', 'text')
        dateTimeOptions = {
            'format': 'dd-mm-yyyy hh:ii ',
            'autoclose': True,
            'showMeridian' : False
            }
        widgets = {
            #NOT Use localization and set a default format
            'end_time': DateTimeWidget(options = dateTimeOptions)
                }

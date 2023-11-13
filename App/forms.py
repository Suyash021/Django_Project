from django import forms
from App.models import Todo
 
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__" 
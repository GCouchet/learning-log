from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):  # hereda .ModelForms de forms
    class Meta:  # The simplest version of a ModelForm consists of a nested Meta class telling Django which model to base the form on and which fields to include in the form
        model = Topic  # we build a form from the Topic model and include only the text field
        fields = ['text']  # que campos del modelo toma
        labels = {'text': ''}  # le dice a djanog que genere una etiqueta pata el campo texto, en este caso que no genere nada


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # es la forma que toma el elemento form, por defecto en django es text
                                                                # pero aca lo hacemos que sea textarea, para que sea un rectangulo mas grande
                                                                # y que tenga 80 columndas, por defecto vienen 40

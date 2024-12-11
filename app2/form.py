from django.forms import ModelForm
from app2.models import table
class studytable(ModelForm):
    class Meta:
        model = table
        fields = '__all__'
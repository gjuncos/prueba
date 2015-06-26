from django import forms

class FormularioPagina(forms.Form):
    asunto=forms.CharField()
    nombre=forms.CharField()
    mail=forms.EmailField()
    departamento=forms.ChoiceField(choices=[("ventas","departamento de Ventas"),("soporte","Departamento de soporte")])
    num_cliente=forms.IntegerField(required=False)
    consulta=forms.CharField(widget=forms.Textarea)
    

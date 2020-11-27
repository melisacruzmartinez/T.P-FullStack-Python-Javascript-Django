from django import forms
from .models import  Producto, Consulta, Pedido, PedidoDetalle, Turnos
# from.models import Turnos
from usuarios.models import User

class ProductoCreate(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if (self.instance.tipo== 'L'):
    #         self.fields['enfoque'].disabled = False
    #         self.fields['lado'].disabled = False
    #         self.fields['armazon'].disabled = False
#_________________________________________________________________________________________     
class TurnosCreate(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = '__all__'
#________________________________________________________________________

class ConsultaCreate(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

class PedidoCreate(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        # para la creación no se necesitan
        exclude=('vendedor', 'estado', 'subtotal', 'fecha')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['vendedor'].disabled = True
        # self.fields['subtotal'].disabled = True
        # self.fields['estado'].value = 'PT'
        # self.fields['estado'].disabled = True
        # self.fields['fecha'].disabled = True
        # self.fields['vendedor'].queryset = User.objects.filter(es_ventas=True)

class PedidoView(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vendedor'].disabled = True
        self.fields['paciente'].disabled = True
        self.fields['tipo_pago'].disabled = True
        self.fields['estado'].disabled = True
        self.fields['subtotal'].disabled = True
        self.fields['fecha'].disabled = True
    
class PedidoUpdate(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        # para update solo cambia el estado
        # exclude=('vendedor', 'paciente', 'tipo_pago', 'subtotal', 'fecha')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)               

class PedidoDetalleCreate(forms.ModelForm):
    class Meta:
        model = PedidoDetalle
        fields = ('producto', 'cantidad')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

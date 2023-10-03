from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate (self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidatorsError({'cpf': "O CPF deve ter 11 dígitos"})
        return data
    # def validate_cpf(self, cpf):
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError("O cpf deve ter 11 dígitos")
    #     return cpf
    
    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não inclua números nesse campo")
    #     return nome
    
    # def validate_rg(self, rg):
    #     if len(rg):
    #         raise serializers.ValidarionError("O rg deve ter 9 dígitos")
    #     return rg
    
    # def validate_celular(self, celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("O celular")
    #     return celular
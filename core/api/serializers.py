
from rest_framework import serializers
from core.models import PontoTuristico, DocIdentificacao
#from atracoes.api.serializers import AtracaoSerializer
#from enderecos.api.serializers import EnderecoSerializer
from rest_framework.fields import SerializerMethodField
from atracoes.models import Atracao
from enderecos.models import Endereco
from enderecos.api.serializers import EnderecoSerializer
from atracoes.api.serializers import AtracaoSerializer



class PontoTuristicoSerializer(serializers.ModelSerializer):

    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = serializers.SerializerMethodField()


    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao','foto','atracoes','endereco','descricao_completa','descricao_completa2')
       
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
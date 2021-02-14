from rest_framework import serializers
from .models import switchhost 
class DeviceSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Role
 #       fields = ('id', 'role')

 class Meta:
    model = switchhost
    fields = ('id','hostname','ipadd')    

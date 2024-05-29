from rest_framework import serializers
from contentmanage.models import ContentList, TDKList

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentList
        fields = '__all__'

class TDKSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDKList
        fields = '__all__'
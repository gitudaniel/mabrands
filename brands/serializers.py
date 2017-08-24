from django.contrib.auth.models import User

from rest_framework import serializers

from brands.models import Info



class InfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False, allow_null=True, required=False)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6, coerce_to_string=False, allow_null=True, required=False)

    class Meta:
        model = Info
        exclude = ('longitude', 'latitude')


    def create(self, validated_data):
        return Info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.collector = validated_data.get('collector', instance.collector)
        instance.interviewee = validated_data.get('interviewee', instance.interviewee)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.favorite = validated_data.get('favorite', instance.favorite)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance




class UserSerializer(serializers.ModelSerializer):
    info = serializers.PrimaryKeyRelatedField(many=True, queryset=Info.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'info')



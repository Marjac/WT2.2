from rest_framework import serializers
from portraits.models import Portrait, LANGUAGE_CHOICES, STYLE_CHOICES

class PortraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portrait
        fields = ('id', 'img', 'title','when', 'what', 'credits', 'description' 'portrait_id')

    def create(self, validated_data):
        """
        Create and return a new `Portrait` instance, given the validated data.
        """
        return Portrait.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Portrait` instance, given the validated data.
        """
        instance.img = validated_data.get('img', instance.img)
        instance.title = validated_data.get('title', instance.title)
        instance.when = validated_data.get('when', instance.when)
        instance.what = validated_data.get('what', instance.what)
        instance.credits = validated_data.get('credits', instance.credits)
        instance.description = validated_data.description('what', instance.description)
        instance.save()
        return instance
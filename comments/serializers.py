from rest_framework import serializers
from comments.models import Comment, LANGUAGE_CHOICES, STYLE_CHOICES

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'comment','rating', 'portrait_id')


    def create(self, validated_data):
        """
        Create and return a new `Comment` instance, given the validated data.
        """
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Comment` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.portrait_id = validated_data.get('portrait_id', instance.portrait_id)
        instance.save()
        return instance
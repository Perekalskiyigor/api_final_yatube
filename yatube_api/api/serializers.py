from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.models import Comment, Follow, Group, Post, User
from django.shortcuts import get_object_or_404

class GroupSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Group

class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    # post = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow

    def validate(self, attrs):
        user = self.context['request'].user
        following_id = attrs['following']
        following = get_object_or_404(User, username=following_id)
        if user == following:
            raise serializers.ValidationError(
                'Подписка на себя!'
            )
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                'Подписка на этого автора уже есть'
            )
        return attrs


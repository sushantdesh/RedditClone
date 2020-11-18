from .models import Posts
from .models import Comment
from django.contrib.auth.models import User
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields= ('ctext', 'upvote', 'downvote', 'owner','date')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    comments=CommentSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Posts
        fields= ('text', 'upvote', 'owner', 'date','comments','ip')




class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Posts.objects.all())
    # posts=PostSerializer(many=True, read_only=True)
    # comments=serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())
    comments=CommentSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']


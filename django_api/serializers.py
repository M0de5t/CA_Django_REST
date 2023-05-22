from rest_framework import serializers
from . models import  Post,PostLike,CommentLike,Comment

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Post
        fields = ['post_id','title','body','user','user_id','created_on']



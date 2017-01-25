#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create by Leo on 15/01/2017


from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from accounts.api.serializers import UserDetailSerializer
from comments.api.serializers import CommentSerializer
from comments.models import Comment

from posts.models import Post


post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='pk'
)

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    # url = HyperlinkedIdentityField(
    #     view_name='posts-api:detail'
    # )
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'publish',
            'url',
        ]


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'markdown',
            'publish',
            'image',
            'url',
            'comments',
        ]

    def get_markdown(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            return None
        return image

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            # 'slug',
            'content',
            'publish'
        ]
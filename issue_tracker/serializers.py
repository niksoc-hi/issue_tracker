from rest_framework import serializers

from issue_tracker import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'username', 'email')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class IssueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue
        exclude = ('description',)


class IssueDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue
        fields = '__all__'

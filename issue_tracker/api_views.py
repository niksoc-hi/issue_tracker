from rest_framework import viewsets

from issue_tracker.serializers import *


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = ProjectSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    filterset_fields = ('project', 'assignee', 'status', 'severity')
    search_fields = ('title',)

    # TODO: search by title (django rest_framework provides this)

    def get_serializer_class(self):
        if self.action == 'list':
            return IssueListSerializer
        return IssueDetailSerializer

from rest_framework import routers

from issue_tracker import api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'projects', api_views.ProjectViewSet)
router.register(r'issues', api_views.IssueViewSet)

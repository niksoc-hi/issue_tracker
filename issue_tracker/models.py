from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(BaseModel):
    name = models.CharField(max_length=63)

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)


class Issue(BaseModel):
    STATUS_OPEN = 'Open'
    STATUS_IN_PROGRESS = 'In Progress'
    STATUS_RESOLVED = 'Resolved'
    STATUSES = (STATUS_OPEN, STATUS_IN_PROGRESS, STATUS_RESOLVED)

    SEVERITY_HIGH = 30
    SEVERITY_MEDIUM = 20
    SEVERITY_LOW = 10
    SEVERITY_CHOICES = (
        (SEVERITY_LOW, 'low'),
        (SEVERITY_MEDIUM, 'medium'),
        (SEVERITY_HIGH, 'high'),
    )

    title = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=zip(STATUSES, STATUSES), max_length=31, default=STATUS_OPEN)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status_updated_at = models.DateTimeField()
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    severity = models.PositiveSmallIntegerField(choices=SEVERITY_CHOICES, default=SEVERITY_MEDIUM)

    def __str__(self):
        return '{}. {}'.format(self.id, self.title)

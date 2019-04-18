from django.db import models

# Create your models here.


class IssueList(models.Model):
    issue = models.CharField(max_length=50)

    def __str__(self):
        return self.issue


class ChioceList(models.Model):
    options = models.CharField(max_length=20)
    number = models.IntegerField(default=0)
    is_issue = models.ForeignKey('IssueList', on_delete=models.CASCADE)

    def __str__(self):
        return self.options


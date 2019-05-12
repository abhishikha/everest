from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=200)
    git_user_name = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')
    git_repo = models.CharField(max_length=200)
    def __str__(self):
        return self.full_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
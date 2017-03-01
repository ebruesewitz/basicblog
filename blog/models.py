# importing models from the django db that stores them
from django.db import models
# need to import timezone to use it in the model.
from django.utils import timezone
# Create your models here.

# blog post data. post contains author, title, content and date published
class Post(models.Model):
    # fk to django's user authentication model. refine/add functionality later.
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    content = models.TextField()
    # no publish date set initially
    published_date = models.DateTimeField(blank = True, null = True)

    # publish method. save post to db and set published date to current date/time
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # return blog title. should I make it a pk?
    def __str__(self):
        return self.title


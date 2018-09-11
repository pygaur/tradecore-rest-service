"""
models user to store post data.
"""

from django.db import models

from user.models import Account

class Post(models.Model):
    """
    To store post details.
    """
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts')

    title = models.CharField(db_index=True, max_length=255)
    description = models.TextField(blank=True)

    added_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        """
        meta properties
        """
        app_label = "post"

    def __str__(self):
        """
        return title
        """
        return self.title


class PostLike(models.Model):
    """
    store likes submitted by users for any post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='post_likes')

    class Meta:
        """
        meta attributes
        """
        unique_together = (('post', 'account'),)

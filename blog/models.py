from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Blog(models.Model):
    title = models.CharField(max_length=150, default='')
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_update_post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Relationship(models.Model):
    from_user = models.ForeignKey("User", related_name="subscriptions")
    to_user = models.ForeignKey("User", related_name="subscribers")
    is_block = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            ('from_user', 'to_user'),
        )


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    about = models.TextField()
    join_date = models.DateTimeField(auto_now_add=True, editable=False)

    # AbstractBaseUser username field definition
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def subscribe(self, subscriber):
        """Add a subscriber to this user."""
        r = Relationship(from_user=subscriber, to_user=self)
        r.save()

    def unsubscribe(self, subscriber):
        sub = self.subscribers.objects.get(from_user=subscriber)
        if sub:
            sub.delete()
            return True
        else:
            return False


class Post(models.Model):
    user = models.ForeignKey("User")
    text = models.TextField()
    post_date = models.DateTimeField()
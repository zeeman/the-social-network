from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class Relationship(models.Model):
    from_user = models.ForeignKey("User")
    to_user = models.ForeignKey("User")
    is_block = models.BooleanField(default=False)


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    about = models.TextField()
    subscribees = models.ManyToManyField(
        "self", through="Relationship", symmetrical=False,
        related_name="subscribed")
    join_date = models.DateTimeField(auto_now_add=True, editable=False)

    # AbstractBaseUser username field definition
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def subscribe(self, subscribee):
        r = Relationship(from_user=self, to_user=subscribee)
        r.save()

    def unsubscribe(self, subscribee):
        sub = self.subscribees.objects.get(to_user=subscribee)
        if sub:
            sub.delete()
            return True
        else:
            return False


class Post(models.Model):
    user = models.ForeignKey("User")
    text = models.TextField()
    post_date = models.DateTimeField()
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models

from net.utils import first


class Relationship(models.Model):
    class Meta:
        app_label = 'net'
        unique_together = (
            ('from_user', 'to_user'),
        )

    from_user = models.ForeignKey("User", related_name="subscriptions")
    to_user = models.ForeignKey("User", related_name="subscribers")
    is_block = models.BooleanField(default=False)

    def __repr__(self):
        return u'<Relationship ({0}): {1} => {2}>'.format(
                'block' if self.is_block else 'subscription',
                self.from_user,
                self.to_user)


class User(AbstractBaseUser):
    class Meta:
        app_label = 'net'

    objects = UserManager()

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    about = models.TextField()
    profile_visibility = models.BooleanField(
        choices=((True, 'Public'), (False, 'Private')), default=False)

    join_date = models.DateTimeField(auto_now_add=True, editable=False)

    # AbstractBaseUser username field definition
    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def subscribe(self, other_user):
        sub = first(self.subscriptions.filter(to_user=other_user))
        if sub:
            return False
        else:
            r = Relationship(from_user=self, to_user=other_user)
            r.save()
            return True

    def unsubscribe(self, other_user):
        sub = first(self.subscriptions.filter(to_user=other_user))
        if sub:
            sub.delete()
            return True
        else:
            return False

    @property
    def friends(self):
        return (
            User.objects.filter(
                pk__in=self.subscribers.values_list('from_user', flat=True)) &
            User.objects.filter(
                pk__in=self.subscriptions.values_list('to_user', flat=True))
        )

    def __unicode__(self):
        return self.name


class Post(models.Model):
    class Meta:
        app_label = 'net'

    user = models.ForeignKey("User", related_name="posts")
    text = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return u'<Post: "{0}">'.format(self.text[:50])

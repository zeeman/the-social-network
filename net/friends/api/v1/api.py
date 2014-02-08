from rest_framework import serializers, viewsets
from net.friends import models as net_models


class RelationshipSerializer(serializers.ModelSerializer):
    from_user = serializers.HyperlinkedRelatedField(many=False, read_only=True,
                                                    view_name="user-detail")
    to_user = serializers.HyperlinkedRelatedField(many=False, read_only=True,
                                                  view_name="user-detail")

    class Meta:
        model = net_models.Relationship


class SubscriptionSerializer(RelationshipSerializer):
    class Meta:
        model = net_models.Relationship
        fields = ['to_user']


class SubscriberSerializer(RelationshipSerializer):
    class Meta:
        model = net_models.Relationship
        fields = ['from_user']


class PostSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='post-detail')
    user = serializers.HyperlinkedRelatedField(many=False, read_only=True,
                                               view_name="user-detail")

    class Meta:
        model = net_models.Post


class PostViewSet(viewsets.ModelViewSet):
    model = net_models.Post
    serializer_class = PostSerializer


class UserSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='user-detail')
    subscriptions = SubscriptionSerializer(many=True)
    subscribers = SubscriberSerializer(many=True)
    posts = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                view_name='post-detail')

    class Meta:
        model = net_models.User
        fields = ['id', 'name', 'about', 'join_date', 'subscriptions',
                  'subscribers', 'posts']


class UserViewSet(viewsets.ModelViewSet):
    model = net_models.User
    serializer_class = UserSerializer
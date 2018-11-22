from rest_framework import serializers
# from rest_framework.serializers import HyperlinkedModelSerializer
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')


    # created = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=100, blank=True, default='')
    # code = models.TextField()
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    # highlighted = models.TextField()



class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')


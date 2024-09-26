from django_filters import FilterSet

from .models import Response, Post


class ResponseFilter(FilterSet):

    def __init__(self, *args, **kwargs):
        super(ResponseFilter, self).__init__(*args, **kwargs)
        self.filters['post'].queryset = Post.objects.filter(author_id=kwargs['request'])
        self.filters['post'].label = 'поиск по объявлению'

    class Meta:
        model = Response
        fields = ('post',)

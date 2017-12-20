from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class SnippetList(generics.ListCreateAPIView):
    #queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get_queryset(self):
        queryset = Snippet.objects.all()
        portrait_id = self.request.query_params.get('portrait_id', None)
        if portrait_id is not None:
            queryset = queryset.filter(portrait_id=portrait_id)
        return queryset


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

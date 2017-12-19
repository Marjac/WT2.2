from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class CommentList(generics.ListCreateAPIView):
    #queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        portrait_id = self.request.query_params.get('portrait_id', None)
        if portrait_id is not None:
            queryset = queryset.filter(portrait_id=portrait_id)
        return queryset


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

from portraits.models import Portrait
from portraits.serializers import PortraitSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class PortraitList(generics.ListCreateAPIView):
    #queryset = Portrait.objects.all()
    serializer_class = PortraitSerializer

    def get_queryset(self):
        queryset = Portrait.objects.all()
        portrait_id = self.request.query_params.get('portrait_id', None)
        if portrait_id is not None:
            queryset = queryset.filter(portrait_id=portrait_id)
        return queryset


class PortraitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portrait.objects.all()
    serializer_class = PortraitSerializer

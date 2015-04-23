import os.path

from django.conf import settings
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import Annotation


def index(request):
    index_file_path = os.path.join(settings.BASE_DIR, 'static', 'index.html')
    with open(index_file_path) as index_file:
        return HttpResponse(index_file.read(), content_type="text/html")


class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        fields = ('id', 'url', 'user', 'start_time', 'end_time', 'text')
        model = Annotation


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super(AnnotationViewSet, self).get_queryset()
        return queryset.filter(user=self.request.user)

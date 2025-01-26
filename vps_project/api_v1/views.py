from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from .serializers import VPSSerializer
from .models import VPS


class VPSFilter(filters.FilterSet):
    class Meta:
        model = VPS
        fields = {
            'uid': ['exact'],
            'cpu': ['gte', 'lte'],
            'ram': ['gte', 'lte'],
            'hdd': ['gte', 'lte'],
            'status': ['exact'],
        }


class VPSViewSet(viewsets.ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ['uid', 'cpu', 'ram', 'hdd', 'status']
    filterset_class = VPSFilter

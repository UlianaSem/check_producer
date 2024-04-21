from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from main import models, serializers


class CheckCreateAPIView(CreateAPIView):
    queryset = models.Check.objects.all()
    serializer_class = serializers.CheckCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        headers = self.get_success_headers(serializers.CheckSerializer(instance).data)
        return Response(serializers.CheckSerializer(instance).data, status=status.HTTP_201_CREATED, headers=headers)

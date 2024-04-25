from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main import models, serializers, producer


class CheckCreateAPIView(CreateAPIView):
    queryset = models.Check.objects.all()
    serializer_class = serializers.CheckCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        data = serializers.CheckSerializer(instance).data
        producer.send_message('check_data', data)

        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

from rest_framework import status, views
from rest_framework.response import Response

from apps.check.models import ChecksModel
from apps.check.serializers import ReceivingCheckSerializer
from produser.produser import send_messages


class ReceivingCheckView(views.APIView):
    """View получения чеков"""

    serializer_class = ReceivingCheckSerializer

    def post(self, request):
        serializer = ReceivingCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_messages(serializer.data)
        ChecksModel.objects.create(json_data=serializer.data)
        return Response('данные в обработке', status=status.HTTP_200_OK)

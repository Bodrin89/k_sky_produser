from django.urls import path

from apps.check.views import ReceivingCheckView

urlpatterns = [
    path('checks/', ReceivingCheckView.as_view(), name='post-check'),
]

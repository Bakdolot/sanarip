from rest_framework import generics, permissions

from .models import Plot
from .serializers import PlotListSerializer


class PlotListView(generics.ListAPIView):
    serializer_class = PlotListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        queryset = Plot.objects.filter(farmer__user=user)
        return queryset

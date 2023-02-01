from rest_framework import serializers

from .models import Plot


class PlotListSerializer(serializers.ModelSerializer):
    culture = serializers.SerializerMethodField()
    season = serializers.SerializerMethodField()
    
    class Meta:
        model = Plot
        fields = ["contour", "culture", "season"]
        
    def get_culture(self, obj):
        return obj.culture.name
    
    def get_season(self, obj):
        return obj.season.name

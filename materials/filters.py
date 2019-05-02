from .models import Station
import django_filters

class StationFilter(django_filters.FilterSet):
    class Meta:
        model = Station
        fields = ['district',]
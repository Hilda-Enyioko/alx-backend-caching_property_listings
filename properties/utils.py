from django.core.cache import cache
from .models import Property

def get_all_properties():
    queryset = cache.get("all_properties")
    
    if queryset is None:
        queryset = Property.objects.all()
        
        cache.set("all_properties", queryset, 3600)
        
    return queryset
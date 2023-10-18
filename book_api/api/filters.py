from rest_framework import filters

class CustomStatusFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        status = request.query_params.get('status', None)
        if status is not None:
            if status.lower() == 'true':
                queryset = queryset.filter(status=True)
            elif status.lower() == 'false':
                queryset = queryset.filter(status=False)
        return queryset
    
class ExactMatchFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        search_param = request.query_params.get('search')
        if search_param:
            return queryset.filter(document_filename=search_param)
        return queryset
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
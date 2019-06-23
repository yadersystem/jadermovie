import django_filters

class MovieFilterDjangoSet(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    year = django_filters.NumberFilter(field_name='release_date',lookup_expr='year')
    release_date = django_filters.DateFromToRangeFilter()
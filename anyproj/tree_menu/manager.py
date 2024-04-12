from anyproj.settings import MENU_MAX_LEVEL
from django.db.models.query import QuerySet, NamedValuesListIterable, FlatValuesListIterable, ValuesListIterable




class MenuQuerySet(QuerySet):

        def values_list(self, *fields, flat=False, named=False):
            super().values_list(*fields, flat=flat, named=named)
            if flat and named:
                raise TypeError("'flat' and 'named' can't be used together.")
            if flat and len(fields) > 1:
                raise TypeError(
                    "'flat' is not valid when values_list is called with more than one "
                    "field."
                )

            field_names = {f for f in fields if not hasattr(f, "resolve_expression")}
            _fields = ['name', 'lvl' ]
            for i in range(0, MENU_MAX_LEVEL):
                _fields.append('parent__' * i + 'slug')
            expressions = {}
            counter = 1
            for field in fields:
                if hasattr(field, "resolve_expression"):
                    field_id_prefix = getattr(
                        field, "default_alias", field.__class__.__name__.lower()
                    )
                    while True:
                        field_id = field_id_prefix + str(counter)
                        counter += 1
                        if field_id not in field_names:
                            break
                    expressions[field_id] = field
                    _fields.append(field_id)
                else:
                    _fields.append(field)

            clone = self._values(*_fields, **expressions)
            clone._iterable_class = (
                NamedValuesListIterable
                if named
                else FlatValuesListIterable if flat else ValuesListIterable
            )
            return clone
        

    
from django.db import models


class YearValueField(models.TextField):
    description = "A field to store a list of objects with 'year' and 'value' as text"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return eval(value)

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return value
        return eval(value)

    def get_prep_value(self, value):
        return str(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

from rest_framework import serializers
from .models import Sessions_overal_statistic, Customer_overal_statistic
import ast


class DateValueTupleField(serializers.ListField):
    def to_internal_value(self, data):
        result = [(item['date'], int(item['value'])) for item in data]
        return result

    def to_representation(self, value):
        return [f'({item[0]}, {item[1]})' for item in value]

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return None


class CustomerOverallStatisticSerializer(serializers.ModelSerializer):
    cust_last_time = DateValueTupleField()

    class Meta:
        model = Customer_overal_statistic
        fields = '__all__'


class SessionOverallStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions_overal_statistic
        fields = '__all__'

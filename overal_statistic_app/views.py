from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sessions_overal_statistic, Customer_overal_statistic
from .serializers import SessionOverallStatisticSerializer, CustomerOverallStatisticSerializer


@api_view(['GET'])
def list_session_overall_statistics(request):
    statistics = Sessions_overal_statistic.objects.all()
    serializer = SessionOverallStatisticSerializer(statistics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_session_overall_statistic(request, session_id):
    try:
        statistic = Sessions_overal_statistic.objects.get(
            session_id=session_id)
    except Sessions_overal_statistic.DoesNotExist:
        return Response(status=404)

    serializer = SessionOverallStatisticSerializer(statistic)
    return Response(serializer.data)


@api_view(['GET'])
def list_customer_overall_statistics(request):
    statistics = Customer_overal_statistic.objects.all()
    serializer = CustomerOverallStatisticSerializer(statistics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_customer_overall_statistic(request, customer_id):
    try:
        statistic = Customer_overal_statistic.objects.get(
            customer_id=customer_id)
    except Customer_overal_statistic.DoesNotExist:
        return Response(status=404)

    serializer = CustomerOverallStatisticSerializer(statistic)
    return Response(serializer.data)

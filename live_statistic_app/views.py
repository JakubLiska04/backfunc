from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sessions_overal_statistic, Customer_overal_statistic
from .serializers import SessionOverallStatisticSerializer, CustomerOverallStatisticSerializer
from rest_framework import status


@api_view(['POST'])
def create_session_and_customer_statistic(request):
    if request.method == 'POST':
        data = request.data
        statistic_type = data.get('statistic_type')

        if statistic_type == 'session':
            session_serializer = SessionOverallStatisticSerializer(data=data)
            if session_serializer.is_valid():
                session_serializer.save()
                return Response({"status": "OK"}, status=status.HTTP_201_CREATED)
            else:
                return Response(session_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif statistic_type == 'customer':
            customer_serializer = CustomerOverallStatisticSerializer(data=data)
            if customer_serializer.is_valid():
                customer_serializer.save()
                return Response({"status": "OK"}, status=status.HTTP_201_CREATED)
            else:
                return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"error": "Invalid statistic_type"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_session_overall_statistics(request):
    session_statistics = Sessions_overal_statistic.objects.all()
    serializer = SessionOverallStatisticSerializer(
        session_statistics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_session_overall_statistic_by_id(request, session_id):
    try:
        session_statistics = Sessions_overal_statistic.objects.get(
            session_id=session_id)
    except Sessions_overal_statistic.DoesNotExist:
        return Response(status=404)

    serializer = SessionOverallStatisticSerializer(session_statistics)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_customer_overall_statistics(request):
    customer_statistics = Customer_overal_statistic.objects.all()
    serializer = CustomerOverallStatisticSerializer(
        customer_statistics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_customer_overall_statistic_by_id(request, customer_id):
    try:
        customer_statistics = Customer_overal_statistic.objects.get(
            customer_id=customer_id)
    except Customer_overal_statistic.DoesNotExist:
        return Response(status=404)

    serializer = CustomerOverallStatisticSerializer(customer_statistics)
    return Response(serializer.data)

from django.urls import path
from .views import create_session_and_customer_statistic, get_all_session_overall_statistics, get_session_overall_statistic_by_id, get_all_customer_overall_statistics, get_customer_overall_statistic_by_id

urlpatterns = [
    path('session_and_customer_statistic/', create_session_and_customer_statistic,
         name='create_session_and_customer_statistic'),
    path('session_overall_statistic/', get_all_session_overall_statistics,
         name='get_all_session_overall_statistics'),
    path('session_overall_statistic/<str:session_id>/',
         get_session_overall_statistic_by_id, name='get_session_overall_statistic_by_id'),
    path('customer_overall_statistic/', get_all_customer_overall_statistics,
         name='get_all_customer_overall_statistics'),
    path('customer_overall_statistic/<str:customer_id>/',
         get_customer_overall_statistic_by_id, name='get_customer_overall_statistic_by_id'),
]

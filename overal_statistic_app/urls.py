from django.urls import path
from . import views

urlpatterns = [
    path('session_overall_statistic/', views.list_session_overall_statistics),
    path('session_overall_statistic/<uuid:session_id>/',
         views.get_session_overall_statistic),
    path('customer_overall_statistic/', views.list_customer_overall_statistics),
    path('customer_overall_statistic/<uuid:customer_id>/',
         views.get_customer_overall_statistic),
]

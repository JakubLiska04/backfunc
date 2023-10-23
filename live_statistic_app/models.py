from django.db import models
import uuid
from .fields import YearValueField


class Sessions_overal_statistic(models.Model):
    session_id = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField(auto_now_add=True)
    session_time = models.IntegerField()
    session_number_of_pages = models.IntegerField()
    session_number_of_clicks = models.IntegerField()
    session_number_of_cta = models.IntegerField()

    def __str__(self):
        return str(self.session_id)


class Customer_overal_statistic(models.Model):
    customer_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField(auto_now_add=True)
    cust_avg_time = models.IntegerField()
    cust_avg_page = models.IntegerField()
    cust_avg_clicks = models.IntegerField()
    cust_avg_cta = models.IntegerField()
    cust_total_num_sessions = models.IntegerField()
    cust_total_num_landing = models.IntegerField()
    cust_total_num_contact = models.IntegerField()
    cust_total_num_pricing = models.IntegerField()
    cust_total_num_signin = models.IntegerField()
    cust_total_num_beforepurchase = models.IntegerField()
    cust_total_num_purchase = models.IntegerField()
    cust_advisory_proc = models.IntegerField(
        choices=((1, '1'), (2, '2'), (3, '3')))
    cust_lifecycle = models.IntegerField(
        choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')))
    cust_ranking = models.IntegerField(
        choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    cust_activity = models.IntegerField(
        choices=((1, '1'), (2, '2'), (3, '3'), (4, '4')))
    cust_last_time = YearValueField()

    def __str__(self):
        return str(self.customer_id)

# Generated by Django 4.2.6 on 2023-10-20 10:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_overal_statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('cust_avg_time', models.IntegerField()),
                ('cust_avg_page', models.IntegerField()),
                ('cust_avg_clicks', models.IntegerField(default=0)),
                ('cust_avg_cta', models.IntegerField()),
                ('cust_total_num_sessions', models.IntegerField()),
                ('cust_total_num_landing', models.IntegerField()),
                ('cust_total_num_contact', models.IntegerField()),
                ('cust_total_num_pricing', models.IntegerField()),
                ('cust_total_num_signin', models.IntegerField()),
                ('cust_total_num_beforepurchase', models.IntegerField()),
                ('cust_total_num_purchase', models.IntegerField()),
                ('cust_advisory_proc', models.IntegerField()),
                ('cust_lifecycle', models.IntegerField()),
                ('cust_ranking', models.IntegerField()),
                ('cust_activity', models.IntegerField()),
                ('cust_last_time', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Sessions_overal_statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('session_time', models.IntegerField()),
                ('session_number_of_pages', models.IntegerField()),
                ('session_number_of_clicks', models.IntegerField()),
                ('session_number_of_cta', models.IntegerField()),
            ],
        ),
    ]
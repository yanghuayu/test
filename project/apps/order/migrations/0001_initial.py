# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('count', models.IntegerField(default=1, verbose_name='\u5546\u54c1\u6570\u76ee')),
                ('price', models.DecimalField(verbose_name='\u5546\u54c1\u4ef7\u683c', max_digits=10, decimal_places=2)),
                ('comment', models.CharField(max_length=256, verbose_name='\u8bc4\u8bba')),
            ],
            options={
                'db_table': 'df_order_goods',
                'verbose_name': '\u8ba2\u5355\u5546\u54c1',
                'verbose_name_plural': '\u8ba2\u5355\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('order_id', models.CharField(max_length=128, serialize=False, verbose_name='\u8ba2\u5355id', primary_key=True)),
                ('pay_method', models.SmallIntegerField(default=3, verbose_name='\u652f\u4ed8\u65b9\u5f0f', choices=[(1, '\u8d27\u5230\u4ed8\u6b3e'), (2, '\u5fae\u4fe1\u652f\u4ed8'), (3, '\u652f\u4ed8\u5b9d'), (4, '\u94f6\u8054\u652f\u4ed8')])),
                ('total_count', models.IntegerField(default=1, verbose_name='\u5546\u54c1\u6570\u91cf')),
                ('total_price', models.DecimalField(verbose_name='\u5546\u54c1\u603b\u4ef7', max_digits=10, decimal_places=2)),
                ('transit_price', models.DecimalField(verbose_name='\u8ba2\u5355\u8fd0\u8d39', max_digits=10, decimal_places=2)),
                ('order_status', models.SmallIntegerField(default=1, verbose_name='\u8ba2\u5355\u72b6\u6001', choices=[(1, '\u5f85\u652f\u4ed8'), (2, '\u5f85\u53d1\u8d27'), (3, '\u5f85\u6536\u8d27'), (4, '\u5f85\u8bc4\u4ef7'), (5, '\u5df2\u5b8c\u6210')])),
                ('trade_no', models.CharField(max_length=128, verbose_name='\u652f\u4ed8\u7f16\u53f7')),
            ],
            options={
                'db_table': 'df_order_info',
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
    ]

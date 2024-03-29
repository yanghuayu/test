# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('name', models.CharField(max_length=20, verbose_name='\u5546\u54c1SPU\u540d\u79f0')),
                ('detail', tinymce.models.HTMLField(verbose_name='\u5546\u54c1\u8be6\u60c5', blank=True)),
            ],
            options={
                'db_table': 'df_goods',
                'verbose_name': '\u5546\u54c1SPU',
                'verbose_name_plural': '\u5546\u54c1SPU',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('image', models.ImageField(upload_to='goods', verbose_name='\u56fe\u7247\u8def\u5f84')),
            ],
            options={
                'db_table': 'df_goods_image',
                'verbose_name': '\u5546\u54c1\u56fe\u7247',
                'verbose_name_plural': '\u5546\u54c1\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='GoodsSKU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('name', models.CharField(max_length=20, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('desc', models.CharField(max_length=256, verbose_name='\u5546\u54c1\u7b80\u4ecb')),
                ('price', models.DecimalField(verbose_name='\u5546\u54c1\u4ef7\u683c', max_digits=10, decimal_places=2)),
                ('unite', models.CharField(max_length=20, verbose_name='\u5546\u54c1\u5355\u4f4d')),
                ('image', models.ImageField(upload_to='goods', verbose_name='\u5546\u54c1\u56fe\u7247')),
                ('stock', models.IntegerField(default=1, verbose_name='\u5546\u54c1\u5e93\u5b58')),
                ('sales', models.IntegerField(default=0, verbose_name='\u5546\u54c1\u9500\u91cf')),
                ('status', models.SmallIntegerField(default=1, verbose_name='\u5546\u54c1\u72b6\u6001', choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')])),
                ('goods', models.ForeignKey(verbose_name='\u5546\u54c1SPU', to='goods.Goods')),
            ],
            options={
                'db_table': 'df_goods_sku',
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('name', models.CharField(max_length=20, verbose_name='\u79cd\u7c7b\u540d\u79f0')),
                ('logo', models.CharField(max_length=20, verbose_name='\u6807\u8bc6')),
                ('image', models.ImageField(upload_to='type', verbose_name='\u5546\u54c1\u7c7b\u578b\u56fe\u7247')),
            ],
            options={
                'db_table': 'df_goods_type',
                'verbose_name': '\u5546\u54c1\u79cd\u7c7b',
                'verbose_name_plural': '\u5546\u54c1\u79cd\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='IndexGoodsBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('image', models.ImageField(upload_to='banner', verbose_name='\u56fe\u7247')),
                ('index', models.SmallIntegerField(default=0, verbose_name='\u5c55\u793a\u987a\u5e8f')),
                ('sku', models.ForeignKey(verbose_name='\u5546\u54c1', to='goods.GoodsSKU')),
            ],
            options={
                'db_table': 'df_index_banner',
                'verbose_name': '\u9996\u9875\u8f6e\u64ad\u5546\u54c1',
                'verbose_name_plural': '\u9996\u9875\u8f6e\u64ad\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='IndexPromotionBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('name', models.CharField(max_length=20, verbose_name='\u6d3b\u52a8\u540d\u79f0')),
                ('url', models.URLField(verbose_name='\u6d3b\u52a8\u94fe\u63a5')),
                ('image', models.ImageField(upload_to='banner', verbose_name='\u6d3b\u52a8\u56fe\u7247')),
                ('index', models.SmallIntegerField(default=0, verbose_name='\u5c55\u793a\u987a\u5e8f')),
            ],
            options={
                'db_table': 'df_index_promotion',
                'verbose_name': '\u4e3b\u9875\u4fc3\u9500\u6d3b\u52a8',
                'verbose_name_plural': '\u4e3b\u9875\u4fc3\u9500\u6d3b\u52a8',
            },
        ),
        migrations.CreateModel(
            name='IndexTypeGoodsBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_delete', models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('display_type', models.SmallIntegerField(default=1, verbose_name='\u5c55\u793a\u7c7b\u578b', choices=[(0, '\u6807\u9898'), (1, '\u56fe\u7247')])),
                ('index', models.SmallIntegerField(default=0, verbose_name='\u5c55\u793a\u987a\u5e8f')),
                ('sku', models.ForeignKey(verbose_name='\u5546\u54c1SKU', to='goods.GoodsSKU')),
                ('type', models.ForeignKey(verbose_name='\u5546\u54c1\u7c7b\u578b', to='goods.GoodsType')),
            ],
            options={
                'db_table': 'df_index_type_goods',
                'verbose_name': '\u4e3b\u9875\u5206\u7c7b\u5c55\u793a\u5546\u54c1',
                'verbose_name_plural': '\u4e3b\u9875\u5206\u7c7b\u5c55\u793a\u5546\u54c1',
            },
        ),
        migrations.AddField(
            model_name='goodssku',
            name='type',
            field=models.ForeignKey(verbose_name='\u5546\u54c1\u79cd\u7c7b', to='goods.GoodsType'),
        ),
        migrations.AddField(
            model_name='goodsimage',
            name='sku',
            field=models.ForeignKey(verbose_name='\u5546\u54c1', to='goods.GoodsSKU'),
        ),
    ]

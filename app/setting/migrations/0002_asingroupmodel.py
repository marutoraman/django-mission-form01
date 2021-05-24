# Generated by Django 3.1.6 on 2021-02-13 00:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsinGroupModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('account_id', models.CharField(max_length=100, verbose_name='アカウントID')),
                ('asin_group_id', models.CharField(max_length=100, verbose_name='ASINグループID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('asin_count', models.IntegerField(default=0, verbose_name='ASIN数')),
                ('completed_count', models.IntegerField(default=0, verbose_name='完了ASIN数')),
                ('completed_at', models.DateTimeField(null=True, verbose_name='完了日時')),
            ],
            options={
                'db_table': 't_asin_group',
            },
        ),
    ]
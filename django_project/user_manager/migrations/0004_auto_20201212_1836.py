# Generated by Django 3.1.4 on 2020-12-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('user_manager', '0003_auto_20201212_1832'),
	]
	
	operations = [
		migrations.AlterField(
				model_name = 'purchase',
				name = 'id',
				field = models.CharField(max_length = 50, primary_key = True, serialize = False),
		),
	]
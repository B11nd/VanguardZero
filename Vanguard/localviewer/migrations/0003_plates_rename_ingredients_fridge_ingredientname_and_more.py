# Generated by Django 4.2.7 on 2023-12-03 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localviewer', '0002_fridge_sensors_remove_event_event_delete_calendar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='plates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlateName', models.CharField(max_length=50)),
                ('Ingredients', models.CharField(max_length=50)),
                ('CookingTime', models.IntegerField()),
                ('Type', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='fridge',
            old_name='Ingredients',
            new_name='IngredientName',
        ),
        migrations.RemoveField(
            model_name='fridge',
            name='PlateName',
        ),
        migrations.RemoveField(
            model_name='fridge',
            name='Time',
        ),
        migrations.RemoveField(
            model_name='fridge',
            name='Type',
        ),
        migrations.AddField(
            model_name='fridge',
            name='Carbs',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fridge',
            name='Complete',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fridge',
            name='Fats',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fridge',
            name='Portion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fridge',
            name='Price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fridge',
            name='Protein',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fridge',
            name='Remaining',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

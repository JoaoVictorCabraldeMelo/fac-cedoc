# Generated by Django 2.0.5 on 2018-06-20 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cedoc', '0009_auto_20180619_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoria')),
                ('video', models.ManyToManyField(to='cedoc.AudioVisual')),
            ],
        ),
        migrations.AlterField(
            model_name='index',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cedoc.CampusJournal'),
        ),
    ]
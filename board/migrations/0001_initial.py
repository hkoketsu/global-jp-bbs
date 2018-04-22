# Generated by Django 2.0.1 on 2018-04-16 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Post title')),
                ('content', models.CharField(max_length=1000, verbose_name='Content')),
                ('poster', models.CharField(max_length=20, verbose_name='Poster')),
                ('post_date', models.DateTimeField(verbose_name='Date posted')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, verbose_name='Content')),
                ('answer_title', models.CharField(max_length=50, verbose_name='Response title')),
                ('respondent', models.CharField(max_length=20, verbose_name='Responder')),
                ('post_date', models.DateTimeField(verbose_name='Date posted')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Post')),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-30 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('option_id', models.AutoField(primary_key=True, serialize=False)),
                ('option_text', models.TextField(max_length=500)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.questions')),
            ],
            options={
                'ordering': ['option_id'],
            },
        ),
    ]

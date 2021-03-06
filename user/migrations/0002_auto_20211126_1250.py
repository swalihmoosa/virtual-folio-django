# Generated by Django 3.2.9 on 2021-11-26 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(default='a', max_length=125),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SkillItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=125)),
                ('item', models.CharField(max_length=125)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.skill')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-05 15:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20190305_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField(default='null')),
                ('endtime', models.DateTimeField(default='null')),
                ('theme', models.CharField(default='null', max_length=200)),
                ('comment', models.TextField(blank=True, default='备注为空', max_length=1000, null=True)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
                ('edittime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '会议',
                'verbose_name_plural': '会议',
                'ordering': ['starttime'],
            },
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('type', models.CharField(default='null', max_length=200)),
                ('comment', models.TextField(blank=True, default='备注为空', max_length=500, null=True)),
                ('addtime', models.DateTimeField(auto_now_add=True)),
                ('edittime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '会议室',
                'verbose_name_plural': '会议室',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='addtime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='edittime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='null', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.user'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='creat_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creat_person', to='management.user', verbose_name='管理员'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='person',
            field=models.ManyToManyField(related_name='person', to='management.user', verbose_name='会议人员'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.room'),
        ),
    ]

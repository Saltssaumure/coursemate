# Generated by Django 2.2.26 on 2022-03-18 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coursemateapp', '0003_auto_20220318_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='Grade',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='PDF',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='student',
        ),
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='coursemateapp.Student'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemateapp.Teacher'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(max_length=10)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemateapp.Student')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemateapp.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Has',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PDF', models.FileField(blank=True, upload_to='')),
                ('Grade', models.FloatField(max_length=10)),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemateapp.Assignment')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemateapp.Student')),
            ],
        ),
    ]
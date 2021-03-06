# Generated by Django 2.2.26 on 2022-03-23 15:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coursemateapp', '0008_auto_20220321_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemateapp.Student'),
        ),
        migrations.AddField(
            model_name='review',
            name='review_ID',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
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
        migrations.AlterField(
            model_name='has',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemateapp.Student'),
        ),
        migrations.AlterField(
            model_name='review',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemateapp.Student'),
        ),
        migrations.AlterField(
            model_name='review',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coursemateapp.Teacher'),
        ),
    ]

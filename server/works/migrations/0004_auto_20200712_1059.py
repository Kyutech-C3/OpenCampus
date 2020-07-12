# Generated by Django 3.0.7 on 2020-07-12 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_liveschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model3d',
            name='sketchfab_id',
        ),
        migrations.AddField(
            model_name='model3d',
            name='gltf',
            field=models.FileField(default='', upload_to='3dmodels/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='model3d',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='works.Model3D'),
        ),
        migrations.AlterField(
            model_name='work',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='works.Game'),
        ),
    ]

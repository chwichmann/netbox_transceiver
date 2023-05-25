# Generated by Django 4.1.9 on 2023-05-25 09:25

from django.db import migrations, models
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0092_delete_jobresult'),
        ('netbox_transceiver', '0004_transceivertypeprofile_transceivertype_profiles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transceivertypeprofile',
            old_name='choice',
            new_name='group',
        ),
        migrations.AddField(
            model_name='transceivertypeprofile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='transceivertypeprofile',
            name='custom_field_data',
            field=models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder),
        ),
        migrations.AddField(
            model_name='transceivertypeprofile',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='transceivertypeprofile',
            name='profile',
            field=models.CharField(default=None, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transceivertypeprofile',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AlterField(
            model_name='transceivertype',
            name='profiles',
            field=models.ManyToManyField(related_name='profiles', to='netbox_transceiver.transceivertypeprofile'),
        ),
    ]

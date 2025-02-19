# Generated by Django 4.0.10 on 2024-10-20 07:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_patient_nhs_no'),
        ('referral', '0005_alter_referral_patient_referraltemp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referraltemp',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='patient.patient'),
        ),
        migrations.CreateModel(
            name='ReferralTemp2',
            fields=[
                ('referral_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('referrer', models.CharField(max_length=20)),
                ('referrer_email', models.CharField(max_length=50)),
                ('reason', models.TextField()),
                ('stage', models.CharField(choices=[('PD', 'Pending review'), ('WL', 'On waiting list'), ('DX', 'Declined'), ('CL', 'Closed'), ('AP', 'Accepted Preston'), ('AB', 'Accepted Blackburn'), ('TP', 'Treatment Preston'), ('TB', 'Treatment Blackburn'), ('CP', 'Completed')], default='PD', max_length=2)),
                ('isOpen', models.BooleanField(default=True)),
                ('date_started', models.DateField(default=datetime.date.today)),
                ('date_closed', models.DateField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='patient.patient')),
            ],
        ),
    ]

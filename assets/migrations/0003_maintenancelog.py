from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_remove_user_is_manager_user_role_historicalasset'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField()),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('asset', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='maintenance_logs',
                    to='assets.asset',
                )),
            ],
        ),
    ]

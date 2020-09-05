# Generated by Django 3.0.6 on 2020-09-05 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketType', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=75)),
                ('description', models.CharField(default='', max_length=1000)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Priority')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Project')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Status')),
                ('ticketType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.TicketType')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('creationDate', models.DateTimeField(verbose_name='creation date')),
                ('ticketID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.CharField(max_length=150)),
                ('creationDate', models.DateTimeField(verbose_name='creation date')),
                ('ticketID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
            ],
        ),
    ]

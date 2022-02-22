# Generated by Django 4.0.2 on 2022-02-22 13:45

from django.db import migrations, models
import django.db.models.deletion
import utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerTyp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FormGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.URLField(max_length=700)),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TimeField()),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.form')),
            ],
        ),
        migrations.CreateModel(
            name='Json',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.JSONField()),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Integer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.ImageField(blank=True, upload_to=utils.image_upload_to)),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.AddField(
            model_name='form',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.formgroup'),
        ),
        migrations.CreateModel(
            name='Float',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FileField(upload_to=utils.image_upload_to)),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DateField()),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Char',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=512)),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Boolean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
                ('required', models.BooleanField(default=False)),
                ('help_text', models.TextField(blank=True, null=True)),
                ('place_holder', models.CharField(blank=True, max_length=215, null=True)),
                ('is_active', models.BooleanField()),
                ('extra_attribute', models.JSONField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answer')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='typ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_builders.answertyp'),
        ),
    ]
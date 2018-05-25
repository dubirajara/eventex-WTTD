# Generated by Django 2.0.3 on 2018-03-14 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('E', 'Email'), ('P', 'Telefone ')],
                                          max_length=1, verbose_name='tipo')),
                ('value', models.CharField(max_length=255, verbose_name='valor')),
            ],
            options={
                'verbose_name': 'contato',
                'verbose_name_plural': 'contatos',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nome')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('photo', models.URLField(verbose_name='foto')),
                ('website', models.URLField(blank=True, verbose_name='website')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'palestrante',
                'verbose_name_plural': 'palestrantes',
            },
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='inicio')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'palestra',
                'verbose_name_plural': 'palestras',
                'ordering': ['start'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('talk_ptr', models.OneToOneField(
                    auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True, primary_key=True, serialize=False, to='core.Talk')),
                ('slots', models.IntegerField()),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
            },
            bases=('core.talk',),
        ),
        migrations.AddField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrante'),
        ),
        migrations.AddField(
            model_name='contact',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='core.Speaker', verbose_name='palestrante'),
        ),
    ]

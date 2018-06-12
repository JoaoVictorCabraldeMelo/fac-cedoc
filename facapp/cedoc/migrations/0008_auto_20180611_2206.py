# Generated by Django 2.0.5 on 2018-06-12 01:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cedoc', '0007_auto_20180601_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusJournal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Untitled', help_text='Name of the Document', max_length=300, verbose_name='Title')),
                ('publisher', models.CharField(default='FAC-UnB', max_length=150, verbose_name='Publisher')),
                ('fileType', models.CharField(choices=[('book', 'Printed Book'), ('.pdf', 'Portable Document Format (PDF)'), ('.mp3', 'MP3 Audio'), ('.wav', 'Microsoft Wave (WAV)'), ('.aif', 'Audio Interchange File Format (AIFF)'), ('.mp4', 'MP4 Format'), ('.mpeg', 'MPEG Format')], default='.txt', max_length=5, verbose_name='File Format')),
                ('coverage', models.CharField(choices=[('L', 'Local'), ('R', 'Regional'), ('I', 'International'), ('N', 'National')], default='R', max_length=2, verbose_name='Coverage')),
                ('rights', models.CharField(default='Free Access', help_text='Access Rights', max_length=100, verbose_name='Rights')),
                ('source', models.CharField(default='Faculdade de Comunicação - FAC', max_length=100, verbose_name='Source')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Document Date')),
                ('fileFormat', models.CharField(choices=[('AN', 'Analog'), ('DG', 'Digital')], default='DG', max_length=2, verbose_name='Media Format')),
                ('submissionDate', models.DateField(auto_now_add=True)),
                ('accepted', models.BooleanField(choices=[(True, 'Sim'), (False, 'Nao')], default=False, verbose_name='Accept file')),
                ('description', models.TextField(blank=True, default='Coleção de jornal de laboratório editado pela Faculdade de Comunicação da UnB.', max_length=300, verbose_name='Description')),
                ('author', models.CharField(default='Jornalismo', max_length=50, verbose_name='Author')),
                ('produtor', models.CharField(default='Faculdade de Comunicação da Universidade de Brasília', max_length=100, verbose_name='Producer')),
                ('editor', models.CharField(default='Faculdade de Comunicação da Universidade de Brasília', max_length=100, verbose_name='Editor')),
                ('collaborator', models.CharField(default='CEDOC', max_length=100, verbose_name='Collaborator')),
                ('language', models.CharField(default='Português', max_length=50, verbose_name='Language')),
                ('license', models.CharField(default='CC BY-NC-ND 4.0', max_length=50, verbose_name='License')),
                ('repoLocation', models.CharField(default='Coleções Especiais - BCE', max_length=100, verbose_name='Location in Collection')),
                ('cedocLocation', models.CharField(default='Arquivo Físico', max_length=100, verbose_name='Location in CEDOC')),
                ('size', models.CharField(default='26.00 x 40.00 cm', help_text='In centimeters', max_length=100, verbose_name='Physical Dimensions')),
                ('File', models.FileField(blank=True, upload_to='texts/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='contributor',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='textfile',
            name='doc_ptr',
        ),
        migrations.RemoveField(
            model_name='audiofile',
            name='doc_ptr',
        ),
        migrations.RemoveField(
            model_name='image',
            name='doc_ptr',
        ),
        migrations.RemoveField(
            model_name='videofile',
            name='doc_ptr',
        ),
        migrations.AddField(
            model_name='audiofile',
            name='accepted',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Nao')], default=False, verbose_name='Accept file'),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='coverage',
            field=models.CharField(choices=[('L', 'Local'), ('R', 'Regional'), ('I', 'International'), ('N', 'National')], default='R', max_length=2, verbose_name='Coverage'),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Document Date'),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='fileFormat',
            field=models.CharField(choices=[('AN', 'Analog'), ('DG', 'Digital')], default='DG', max_length=2, verbose_name='Media Format'),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='fileType',
            field=models.CharField(choices=[('book', 'Printed Book'), ('.pdf', 'Portable Document Format (PDF)'), ('.mp3', 'MP3 Audio'), ('.wav', 'Microsoft Wave (WAV)'), ('.aif', 'Audio Interchange File Format (AIFF)'), ('.mp4', 'MP4 Format'), ('.mpeg', 'MPEG Format')], default='.txt', max_length=5, verbose_name='File Format'),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='audiofile',
            name='publisher',
            field=models.CharField(default='FAC-UnB', max_length=150, verbose_name='Publisher'),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='rights',
            field=models.CharField(default='Free Access', help_text='Access Rights', max_length=100, verbose_name='Rights'),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='source',
            field=models.CharField(default='Faculdade de Comunicação - FAC', max_length=100, verbose_name='Source'),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='submissionDate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='audiofile',
            name='title',
            field=models.CharField(default='Untitled', help_text='Name of the Document', max_length=300, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='image',
            name='accepted',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Nao')], default=False, verbose_name='Accept file'),
        ),
        migrations.AddField(
            model_name='image',
            name='coverage',
            field=models.CharField(choices=[('L', 'Local'), ('R', 'Regional'), ('I', 'International'), ('N', 'National')], default='R', max_length=2, verbose_name='Coverage'),
        ),
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Document Date'),
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='image',
            name='fileFormat',
            field=models.CharField(choices=[('AN', 'Analog'), ('DG', 'Digital')], default='DG', max_length=2, verbose_name='Media Format'),
        ),
        migrations.AddField(
            model_name='image',
            name='fileType',
            field=models.CharField(choices=[('book', 'Printed Book'), ('.pdf', 'Portable Document Format (PDF)'), ('.mp3', 'MP3 Audio'), ('.wav', 'Microsoft Wave (WAV)'), ('.aif', 'Audio Interchange File Format (AIFF)'), ('.mp4', 'MP4 Format'), ('.mpeg', 'MPEG Format')], default='.txt', max_length=5, verbose_name='File Format'),
        ),
        migrations.AddField(
            model_name='image',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='publisher',
            field=models.CharField(default='FAC-UnB', max_length=150, verbose_name='Publisher'),
        ),
        migrations.AddField(
            model_name='image',
            name='rights',
            field=models.CharField(default='Free Access', help_text='Access Rights', max_length=100, verbose_name='Rights'),
        ),
        migrations.AddField(
            model_name='image',
            name='source',
            field=models.CharField(default='Faculdade de Comunicação - FAC', max_length=100, verbose_name='Source'),
        ),
        migrations.AddField(
            model_name='image',
            name='submissionDate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='Untitled', help_text='Name of the Document', max_length=300, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='accepted',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Nao')], default=False, verbose_name='Accept file'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='coverage',
            field=models.CharField(choices=[('L', 'Local'), ('R', 'Regional'), ('I', 'International'), ('N', 'National')], default='R', max_length=2, verbose_name='Coverage'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Document Date'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='fileFormat',
            field=models.CharField(choices=[('AN', 'Analog'), ('DG', 'Digital')], default='DG', max_length=2, verbose_name='Media Format'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='fileType',
            field=models.CharField(choices=[('book', 'Printed Book'), ('.pdf', 'Portable Document Format (PDF)'), ('.mp3', 'MP3 Audio'), ('.wav', 'Microsoft Wave (WAV)'), ('.aif', 'Audio Interchange File Format (AIFF)'), ('.mp4', 'MP4 Format'), ('.mpeg', 'MPEG Format')], default='.txt', max_length=5, verbose_name='File Format'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videofile',
            name='publisher',
            field=models.CharField(default='FAC-UnB', max_length=150, verbose_name='Publisher'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='rights',
            field=models.CharField(default='Free Access', help_text='Access Rights', max_length=100, verbose_name='Rights'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='source',
            field=models.CharField(default='Faculdade de Comunicação - FAC', max_length=100, verbose_name='Source'),
        ),
        migrations.AddField(
            model_name='videofile',
            name='submissionDate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videofile',
            name='title',
            field=models.CharField(default='Untitled', help_text='Name of the Document', max_length=300, verbose_name='Title'),
        ),
        migrations.DeleteModel(
            name='Contributor',
        ),
        migrations.DeleteModel(
            name='Doc',
        ),
        migrations.DeleteModel(
            name='TextFile',
        ),
    ]

from django.db import models
import datetime
import django
################################# ACCEPTED FILE TYPES
def getFileTypes():
    return (
        ('book', 'Printed Book'),
        ('.pdf', 'Portable Document Format (PDF)'),
        ('.mp3', 'MP3 Audio'),
        ('.wav', 'Microsoft Wave (WAV)'),
        ('.aif', 'Audio Interchange File Format (AIFF)'),
        ('.mp4', 'MP4 Format'),
        ('.mpeg', 'MPEG Format'),
    )

def getFileFormat():
    return (
        ('AN', 'Analog'),
        ('DG', 'Digital')
    )

def coverage():
    return (
        ('L', 'Local'),
        ('R', 'Regional'),
        ('I', 'International'),
        ('N', 'National')
    )

def accept():
    return(
        (True, 'Sim'),
        (False, 'Nao'),
    )
    
# Create your models here.
class Doc(models.Model):
    id = models.AutoField(primary_key=True)
    # TITLE START - includes many fields
    title = models.CharField('Title', max_length=300, default='Untitled', help_text="Name of the Document")
    description = models.TextField('Description', blank=True)
    publisher = models.CharField('Publisher', max_length=150, default="FAC-UnB")
    # TODO: create options specific for each kind of document
    fileType = models.CharField('File Format', max_length=5, default='.txt', choices=getFileTypes())
    coverage = models.CharField('Coverage', max_length=2, default='R', choices=coverage())
    rights = models.CharField('Rights', max_length=100, default='Free Access', help_text="Access Rights")
    source = models.CharField('Source', default='Faculdade de Comunicação - FAC' , max_length=100)
    date = models.DateField('Document Date', default=django.utils.timezone.now)
    fileFormat = models.CharField('Media Format', max_length=2, choices=getFileFormat(), default='DG')
    submissionDate = models.DateField(auto_now_add=True)
    accepted = models.BooleanField('Accept file', choices=accept(), default=False)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

# TODO: ask what's the best way to implement this
#class Contributor(models.Model):
#    contributor = models.CharField(max_length=100)
#    role = models.CharField(max_length=100, default="Contributor")
#    paper = models.ManyToManyField(Doc)
  
class Image(Doc):
    Image = models.ImageField(upload_to='images/', blank=True)

class CampusJournal(Doc):
    description = models.TextField('Description', max_length=300, blank=True, default='Coleção de jornal de laboratório editado pela Faculdade de Comunicação da UnB.')
    author = models.CharField('Author', max_length=50, default='Jornalismo')
    produtor = models.CharField('Producer', max_length=100, default="Faculdade de Comunicação da Universidade de Brasília")
    editor = models.CharField('Editor', max_length=100, default="Faculdade de Comunicação da Universidade de Brasília")
    collaborator = models.CharField('Collaborator', max_length=100, default="CEDOC")
    language = models.CharField('Language', max_length=50, default='Português')
    license = models.CharField('License', max_length=50, default='CC BY-NC-ND 4.0')
    repoLocation = models.CharField('Location in Collection', max_length=100, default='Coleções Especiais - BCE')
    cedocLocation = models.CharField('Location in CEDOC', max_length=100, default='Arquivo Físico')
    size = models.CharField('Physical Dimensions', max_length=100, default='26.00 x 40.00 cm', help_text='In centimeters')
    File = models.FileField(upload_to='texts/', blank=True)

class AudioFile(Doc):
    duration = models.DurationField('Audio Duration', default=datetime.timedelta(0))
    language = models.CharField('Language', max_length=50, default='None', blank=True)
    File = models.FileField(upload_to='audio/', blank=True)

class VideoFile(Doc):
    duration = models.DurationField('Video Duration', default=datetime.timedelta(0))
    language = models.CharField('Language', max_length=50, default='None', blank=True)
    File = models.FileField(upload_to='video/', blank=True)
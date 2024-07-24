from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.

SCHOOLTYPE_CHOICES = (
    ('university','university'),
    ('polytechnic', "polytechnic"),
    ('college', "college")
)

class CampusAVS(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50, unique=True, verbose_name ='Campus or institution Acronym')
    campusName = models.CharField(max_length=150, verbose_name ='Campus Full name')
    institutionType = models.CharField(max_length=50, choices=SCHOOLTYPE_CHOICES, verbose_name ='Type of Institution')
    about = models.TextField()
    fellowship_facebook_link = models.URLField(blank=True, null=True, verbose_name ='Fellowship Facebook link')
    fellowship_instagram_link = models.URLField(blank=True, null=True, verbose_name ='Fellowship Instagram Link')
    fellowship_email = models.CharField(max_length=50, blank=True, verbose_name ='Campus Fellowship Email Address')
    fellowship_phone_number = models.CharField(max_length=50,  blank=True, verbose_name ='Campus Fellowship Phone number')
    flyer = models.ImageField(upload_to="campus_avs_images/", blank=True)

    bibleStudyTime = models.CharField(max_length=50, blank=True, verbose_name ='Bible Study Time')
    bibleStudyVenue = models.TextField(blank=True, verbose_name ='Bible Study Venue')

    fellowshipTime = models.CharField(max_length=50, blank=True, verbose_name ='Fellowship Time')
    fellowshipVenue = models.TextField(blank=True, verbose_name ='Fellowship Venue')

    OtherScheduleOfServiceDetails = models.TextField(blank=True, verbose_name ='Other Fellowship Service Details')

    averageNumberOfStudent = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Average number of Student')
    numberOfWorkforce = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name ='Total number of workforce')

    joinAlumiGroup = models.URLField(blank=True, null=True, verbose_name ='Link to join Alumni Group')


    coordinator_name = models.CharField(max_length=300, blank=True, null=True, verbose_name ='Coordinator name')
    coordinator_picture = models.ImageField(upload_to="campus_avs_images_cord/", height_field=None, width_field=None, max_length=None, blank=True, verbose_name ='Upload Coordinator picture')
    coordinator_course = models.CharField(max_length=800, blank=True, null=True, verbose_name ='Coordinator Course')
    coordinator_level = models.CharField(max_length=50, blank=True, null=True, verbose_name ='Coordinator Level Or program')
    coordinator_email = models.EmailField(max_length=254, blank=True, null=True, verbose_name ='Coordinator email')
    coordinator_phonenumber = models.CharField(max_length=50, blank=True, null=True, verbose_name ='Coordinator Phone number')


    secretary_name = models.CharField(max_length=300, blank=True, null=True, verbose_name ='Secretary name')
    secretary_picture = models.ImageField(upload_to="campus_avs_images_sect/", height_field=None, width_field=None, max_length=None, blank=True, verbose_name ='Upload Secretary Picture')
    secretary_course = models.CharField(max_length=800, blank=True, null=True, verbose_name ='Secretary course')
    secretary_level = models.CharField(max_length=50, blank=True, null=True, verbose_name ='Secretary Level or program')
    secretary_email = models.EmailField(max_length=254, blank=True, null=True, verbose_name ='Secretary email')
    secretary_phonenumber = models.CharField(max_length=50, blank=True, null=True, verbose_name ='Secretary Phone number')


    posted = models.DateTimeField(
        auto_now=False, auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.campusOrSchoolAcronym
    class Meta:
        verbose_name_plural = 'Campus AVS'

PROGRAM_CHOICES = (
    ('revival_program','National Revival Program (NRP)'),
    ('welcome_program', "Fresher's Welcome Program")
)

class CampusAVSReport(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50)
    program_type = models.CharField(max_length=50, choices=PROGRAM_CHOICES) # welcome_program or revival_program
    year = models.CharField(max_length=50, blank=True)
    salvation = models.CharField(max_length=50, blank=True)
    sanctification = models.CharField(max_length=50, blank=True)
    baptism = models.CharField(max_length=50, blank=True)
    healing = models.CharField(max_length=50, blank=True)
    TotalAttendanceMale = models.CharField(max_length=50, blank=True)
    TotalAttendanceFemale = models.CharField(max_length=50, blank=True)
    TotalAttendance = models.CharField(max_length=50, blank=True)
    body = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.campusOrSchoolAcronym
    class Meta:
        verbose_name_plural = 'Campus AVS Report'


class ReportImage(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50, blank=False)
    program_type = models.CharField(max_length=50, choices=PROGRAM_CHOICES, blank=False) # welcome_program or revival_program
    picture1 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage())
    picture2 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage())
    picture3 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage())
    picture4 = models.FileField(upload_to="report_images/", storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return self.campusOrSchoolAcronym

    class Meta:
        verbose_name_plural = 'Campus AVS Report Images'


class HistoryImage(models.Model):
    campusOrSchoolAcronym = models.CharField(max_length=50, blank=False)
    picture = models.FileField(upload_to="history_images/", storage=RawMediaCloudinaryStorage())

    def __str__(self):
        return self.campusOrSchoolAcronym

    class Meta:
        verbose_name_plural = 'Campus AVS Historical Pictures'


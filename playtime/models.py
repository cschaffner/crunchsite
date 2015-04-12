from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=100, null=True)
    location = models.ForeignKey('FieldLocation')

    def __unicode__(self):
       return self.location.name + ": " + self.name


class FieldLocation(models.Model):
    name = models.CharField(max_length=100, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    address = models.TextField(null=True)

    def __unicode__(self):
        return 'Location: ' + self.name


class FieldSlot(models.Model):
    name = models.CharField(max_length=100, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __unicode__(self):
       return self.name


class FieldEvent(models.Model):
    name = models.CharField(max_length=100, null=True)
    fields = models.ForeignKey('Field')
    field_slot = models.ForeignKey('FieldSlot')
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
       return self.name



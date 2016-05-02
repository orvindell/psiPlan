from __future__ import unicode_literals

from django.db import models


class Daysofweek(models.Model):
    dayofweekname = models.CharField(db_column='dayOfWeekName', max_length=45)  # Field name made lowercase.
    dayofweekshortname = models.CharField(db_column='dayOfWeekShortName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daysOfWeek'


class Departments(models.Model):
    departmentname = models.CharField(db_column='departmentName', max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departments'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Groups(models.Model):
    groupparentid = models.IntegerField(db_column='groupParentId')  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=120)  # Field name made lowercase.
    groupsemester = models.IntegerField(db_column='groupSemester')  # Field name made lowercase.
    groupdepartmentid = models.ForeignKey(Departments, models.DO_NOTHING, db_column='groupDepartmentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'groups'


class Lecturefrequenceparity(models.Model):
    idofparity = models.IntegerField(db_column='idOfParity', primary_key=True)  # Field name made lowercase.
    nameofparity = models.CharField(db_column='nameOfParity', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lectureFrequenceParity'


class Lecturetypes(models.Model):
    lecturename = models.CharField(db_column='lectureName', max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lectureTypes'


class Room(models.Model):
    idofroom = models.IntegerField(db_column='idOfRoom', primary_key=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='roomName', max_length=45)  # Field name made lowercase.
    roomnumber = models.CharField(db_column='roomNumber', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'





class Teachers(models.Model):
    title = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=250)
    departmentid = models.CharField(db_column='departmentId', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachers'


class Teacherworkingplan(models.Model):
    teacherid = models.ForeignKey(Teachers, models.DO_NOTHING, db_column='teacherId')  # Field name made lowercase.
    dayofweekid = models.ForeignKey(Daysofweek, models.DO_NOTHING, db_column='dayOfWeekId')  # Field name made lowercase.
    timestart = models.TimeField(db_column='timeStart')  # Field name made lowercase.
    timestop = models.TimeField(db_column='timeStop')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacherWorkingPlan'

class Lectures(models.Model):
    lectureleadersid = models.ManyToManyField(Teachers, db_column='lectureleadersid')
    lecturedayofweekid = models.ForeignKey(Daysofweek, models.DO_NOTHING, db_column='lectureDayOfWeekId')  # Field name made lowercase.
    lecturetypeid = models.ForeignKey(Lecturetypes, models.DO_NOTHING, db_column='lectureTypeId')  # Field name made lowercase.
    lecturegroupid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='lectureGroupId')  # Field name made lowercase.
    lecutrefrequenceparityid = models.ForeignKey(Lecturefrequenceparity, models.DO_NOTHING, db_column='lecutreFrequenceParityId')  # Field name made lowercase.
    lectureroomsid = models.ManyToManyField(Room, db_column='lectureroomsid')

    lecturename = models.CharField(db_column='lectureName', max_length=120)  # Field name made lowercase.
    lecturefrequence = models.IntegerField(db_column='lectureFrequence')  # Field name made lowercase.
    lecturetimestart = models.TimeField(db_column='lectureTimeStart')  # Field name made lowercase.
    lecturetimestop = models.TimeField(db_column='lectureTimeStop')  # Field name made lowercase.
    lectureannotiation = models.CharField(db_column='lectureAnnotiation', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lectures'



from __future__ import unicode_literals

from django.db import models


class Daysofweek(models.Model):
    idofweek = models.AutoField(db_column='idOfWeek', primary_key=True)  # Field name made lowercase.
    dayofweekname = models.CharField(db_column='dayOfWeekName', max_length=45)  # Field name made lowercase.
    dayofweekshortname = models.CharField(db_column='dayOfWeekShortName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'daysOfWeek'


class Departments(models.Model):
    idofdepartment = models.AutoField(db_column='idOfDepartment', primary_key=True)  # Field name made lowercase.
    departmentname = models.CharField(db_column='departmentName', max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departments'


class Groups(models.Model):
    idgroup = models.AutoField(db_column='idGroup', primary_key=True)  # Field name made lowercase.
    groupparentid = models.IntegerField(db_column='groupParentId')  # Field name made lowercase.
    groupname = models.CharField(db_column='groupName', max_length=120)  # Field name made lowercase.
    groupsemester = models.IntegerField(db_column='groupSemester')  # Field name made lowercase.
    groupprofileid = models.ForeignKey('Profiles', db_column='groupProfileId')  # Field name made lowercase.
    groupdepartmentid = models.ForeignKey(Departments, db_column='groupDepartmentId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'groups'
        unique_together = ['idgroup', 'groupdepartmentid', 'groupprofileid']


class Lecturefrequenceparity(models.Model):
    idofparity = models.IntegerField(db_column='idOfParity', primary_key=True)  # Field name made lowercase.
    nameofparity = models.CharField(db_column='nameOfParity', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lectureFrequenceParity'


class Lectureleaders(models.Model):
    idlectureleaders = models.AutoField(db_column='idLectureLeaders', primary_key=True)  # Field name made lowercase.
    teacherid = models.ForeignKey('Teachers', db_column='teacherId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lectureLeaders'
        unique_together = ['idlectureleaders', 'teacherid']


class Lecturerooms(models.Model):
    idofrooms = models.AutoField(db_column='idOfRooms', primary_key=True)  # Field name made lowercase.
    roomid = models.ForeignKey('Room', db_column='roomId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lectureRooms'
        unique_together = ['idofrooms', 'roomid']


class Lecturetypes(models.Model):
    idoflecturetype = models.AutoField(db_column='idOfLectureType', primary_key=True)  # Field name made lowercase.
    lecturename = models.CharField(db_column='lectureName', max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lectureTypes'


class Lectures(models.Model):
    idoflectures = models.AutoField(db_column='idOfLectures', primary_key=True)  # Field name made lowercase.
    lectureleadersid = models.ForeignKey(Lectureleaders, db_column='lectureLeadersId')  # Field name made lowercase.
    lecturedayofweekid = models.ForeignKey(Daysofweek, db_column='lectureDayOfWeekId')  # Field name made lowercase.
    lecturename = models.CharField(db_column='lectureName', max_length=120)  # Field name made lowercase.
    lecturetypeid = models.ForeignKey(Lecturetypes, db_column='lectureTypeId')  # Field name made lowercase.
    lecturegroupid = models.ForeignKey(Groups, db_column='lectureGroupId')  # Field name made lowercase.
    lecturefrequence = models.IntegerField(db_column='lectureFrequence')  # Field name made lowercase.
    lecutrefrequenceparityid = models.ForeignKey(Lecturefrequenceparity, db_column='lecutreFrequenceParityId')  # Field name made lowercase.
    lectureroomsid = models.ForeignKey(Lecturerooms, db_column='lectureRoomsId')  # Field name made lowercase.
    lecturetimestart = models.TimeField(db_column='lectureTimeStart')  # Field name made lowercase.
    lecturetimestop = models.TimeField(db_column='lectureTimeStop')  # Field name made lowercase.
    lectureannotiation = models.CharField(db_column='lectureAnnotiation', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'lectures'
        unique_together = ['idoflectures', 'lecturedayofweekid', 'lecturegroupid', 'lectureleadersid', 'lecturetypeid', 'lecutrefrequenceparityid', 'lecutrefrequenceparityid']


class Profiles(models.Model):
    idofprofile = models.AutoField(db_column='idOfProfile', primary_key=True)  # Field name made lowercase.
    profilename = models.CharField(db_column='profileName', max_length=120)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'profiles'


class Room(models.Model):
    idofroom = models.IntegerField(db_column='idOfRoom', primary_key=True)  # Field name made lowercase.
    roomname = models.CharField(db_column='roomName', max_length=45)  # Field name made lowercase.
    roomnumber = models.CharField(db_column='roomNumber', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'room'


class Teacherworkingplan(models.Model):
    teacherid = models.ForeignKey('Teachers', db_column='teacherId', primary_key=True)  # Field name made lowercase.
    dayofweekid = models.ForeignKey(Daysofweek, db_column='dayOfWeekId')  # Field name made lowercase.
    timestart = models.TimeField(db_column='timeStart')  # Field name made lowercase.
    timestop = models.TimeField(db_column='timeStop')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'teacherWorkingPlan'
        unique_together = ['teacherid', 'dayofweekid']


class Teachers(models.Model):
    idofteacher = models.AutoField(db_column='idOfTeacher', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=250)
    departmentid = models.CharField(db_column='departmentId', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachers'

class Person(models.Model):
    title = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
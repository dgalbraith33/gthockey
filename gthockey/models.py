from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    FORWARD = 'F'
    DEFENSE = 'D'
    GOALIE = 'G'
    POSITION_CHOICES = (
        (FORWARD, 'F'),
        (DEFENSE, 'D'),
        (GOALIE, 'G'),
    )
    position = models.CharField(max_length=1,
                                choices=POSITION_CHOICES,
                                default=FORWARD)

    number = models.IntegerField(null=True, blank=True)
    hometown = models.CharField(max_length=50,
                                blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Game(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True,
                            blank=True)
    opponent = models.ForeignKey('Team',
                                 null=True,
                                 blank=True)

    HOME = 'H'
    AWAY = 'A'
    TOURNAMENT = 'T'
    VENUE_CHOICES = (
        (HOME, 'Home'),
        (AWAY, 'Away'),
        (TOURNAMENT, 'Tournament'),
    )
    venue = models.CharField(max_length=1,
                             choices=VENUE_CHOICES,
                             default=HOME)
    location = models.ForeignKey('Rink',
                                 null=True,
                                 blank=True)

    class Meta:
        ordering = ['-date', '-time']

    def get_venue(self):
        vdict = {
            "H": "home",
            "A": "away",
            "T": "tournament"
        }
        return vdict[self.venue]

    def get_time(self):
        if self.time:
            return self.time.strftime("%I:%M %p").strip("0")
        else:
            return "TBD"

    def get_rink_name(self):
        if self.location:
            return self.location.rink_name
        else:
            return "TBD"

    def __str__(self):
        return "vs " + str(self.opponent)


class Team(models.Model):
    school_name = models.CharField(max_length=50)
    mascot_name = models.CharField(max_length=50,
                                   blank=True)
    web_url = models.CharField(max_length=100,
                               blank=True)

    class Meta:
        ordering = ['school_name']

    def __str__(self):
        return self.school_name


class Rink(models.Model):
    rink_name = models.CharField(max_length=50)
    maps_url = models.CharField(max_length=100,
                                blank=True)

    def __str__(self):
        return self.rink_name

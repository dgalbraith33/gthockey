from django.db import models
from datetime import date

class Player(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    FORWARD = 'F'
    DEFENSE = 'D'
    GOALIE = 'G'
    MANAGER = 'M'
    POSITION_CHOICES = (
        (FORWARD, 'F'),
        (DEFENSE, 'D'),
        (GOALIE, 'G'),
        (MANAGER, 'M')
    )
    position = models.CharField(max_length=1,
                                choices=POSITION_CHOICES,
                                default=FORWARD)

    number = models.IntegerField(null=True, blank=True)
    hometown = models.CharField(max_length=50,
                                blank=True)
    school = models.CharField(max_length=50,
                                blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Game(models.Model):
    HOME = 'H'
    AWAY = 'A'
    TOURNAMENT = 'T'
    VENUE_CHOICES = (
        (HOME, 'Home'),
        (AWAY, 'Away'),
        (TOURNAMENT, 'Tournament'),
    )

    UPCOMING = "Upcoming"

    date = models.DateField()
    time = models.TimeField(null=True,
                            blank=True)
    opponent = models.ForeignKey('Team',
                                 null=True,
                                 blank=True)

    venue = models.CharField(max_length=1,
                             choices=VENUE_CHOICES,
                             default=HOME)
    location = models.ForeignKey('Rink',
                                 null=True,
                                 blank=True)
    season = models.ForeignKey('Season',
                               null=True,
                               blank=True)

    score_gt_first = models.IntegerField(null=True, blank=True)
    score_gt_second = models.IntegerField(null=True, blank=True)
    score_gt_third = models.IntegerField(null=True, blank=True)
    score_gt_ot = models.IntegerField(null=True, blank=True)
    score_gt_final = models.IntegerField(null=True, blank=True)
    score_opp_first = models.IntegerField(null=True, blank=True)
    score_opp_second = models.IntegerField(null=True, blank=True)
    score_opp_third = models.IntegerField(null=True, blank=True)
    score_opp_ot = models.IntegerField(null=True, blank=True)
    score_opp_final = models.IntegerField(null=True, blank=True)

    period = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)

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

    def get_result(self):
        if self.period == 0 and self.date >= date.today():
            return "Upcoming"

        if self.score_gt_final is None or self.score_opp_final is None:
            return "Not Yet Reported"

        if self.score_gt_final > self.score_opp_final:
            return "Win"

        if self.score_opp_ot is not None and self.score_gt_ot is not None and \
                        self.score_opp_ot > self.score_gt_ot:
            return "Overtime Loss"

        if self.score_opp_final > self.score_gt_final:
            return "Loss"

        if self.score_opp_final == self.score_gt_final:
            return "Tie"

        if self.period == 6:
            return "Cancelled"

        return "Not Yet Reported"

    def get_short_result(self):
        trans = {
            "Upcoming": "U",
            "Win": "W",
            "Overtime Loss": "OT",
            "Loss": "L",
            "Tie": "T",
            "Cancelled": "C",
            "Not Yet Reported": "N"
        }

        return trans[self.get_result()]


    def __str__(self):
        return "vs " + str(self.opponent)


class Team(models.Model):
    school_name = models.CharField(max_length=50)
    mascot_name = models.CharField(max_length=50,
                                   blank=True)
    web_url = models.CharField(max_length=100,
                               blank=True)

    logo = models.ImageField(upload_to='teamlogos', blank=True)

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


class NewsStory(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to="news")
    content = models.CharField(max_length=10000, blank=True)

    def has_content(self):
        return self.content is not None \
               and len(self.content) > 0

    def content_p(self):
        formatted = ""
        paras = self.content.split("\n")
        for line in paras:
            formatted += "<p>"
            formatted += line
            formatted += "</p>"

        return formatted

    def get_absolute_url(self):
        return "/news/%i/" % self.id


# Simple model to hold emails in the database rather than commit them to prevent them from being scraped
class Email(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)


class Season(models.Model):
    name = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_current():
        return Season.objects.order_by("-year")[0]

class Board(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    position = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to="board")
    description = models.CharField(max_length=1000)
    priority = models.IntegerField()

class Coach(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    coach_position = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to="coach")
    bio = models.CharField(max_length=1000)
    priority = models.IntegerField()

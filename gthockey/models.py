from django.db import models
from datetime import datetime, time


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
                                 blank=True,
                                 on_delete=models.SET_NULL)

    venue = models.CharField(max_length=1,
                             choices=VENUE_CHOICES,
                             default=HOME)
    location = models.ForeignKey('Rink',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    season = models.ForeignKey('Season',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)

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

    @property
    def datetime(self):
        temp_time = self.time or time(0)
        return datetime.combine(self.date, temp_time)

    def get_time(self):
        if self.time:
            return self.time.strftime("%I:%M %p").strip("0")
        else:
            return "TBD"

    def opponent_name(self):
        if self.opponent:
            return self.opponent.school_name
        else:
            return None

    def rink_name(self):
        if self.location:
            return self.location.rink_name
        else:
            return "TBD"

    def get_result(self):
        if self.datetime >= datetime.now():
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

    @property
    def short_result(self):
        short_version = {
            "Upcoming": "U",
            "Win": "W",
            "Overtime Loss": "OT",
            "Loss": "L",
            "Tie": "T",
            "Cancelled": "C",
            "Not Yet Reported": "?"
        }

        return short_version[self.get_result()]

    @property
    def is_reported(self):
        return self.score_gt_final is not None and self.score_opp_final is not None

    @property
    def gt_score(self):
        return self.score_gt_final

    @property
    def opp_score(self):
        return self.score_opp_final

    @property
    def season_name(self):
        return self.season.name

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


# Simple model to hold emails in the database rather than commit them to prevent them from being
# scraped from github
class Email(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    active = models.BooleanField(default=True)


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


class ShopItem(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="shop")
    visible = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)


class ShopItemOptionList(models.Model):
    shop_item = models.ForeignKey(ShopItem, related_name='options', on_delete=models.CASCADE)
    display_name = models.CharField(max_length=25)
    help_text = models.CharField(max_length=50, blank=True)
    option_list = models.CharField(max_length=100)


class ShopItemCustomOption(models.Model):
    shop_item = models.ForeignKey(ShopItem, related_name='custom_options', on_delete=models.CASCADE)
    display_name = models.CharField(max_length=25)
    help_text = models.CharField(max_length=50, blank=True)
    required = models.BooleanField(default=False)
    extra_cost = models.FloatField(blank=True)


class ShopItemImage(models.Model):
    shop_item = models.ForeignKey(ShopItem, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="shop")

from rest_framework import serializers
from gthockey.models import Player, Game, NewsStory


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name', 'position', 'number', 'hometown', 'school')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'date', 'time', 'opponent', 'venue', 'location', 'season', 'score_gt_final', 'score_opp_final', 'short_result')
        depth = 1


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStory
        fields = ('id', 'title', 'date', 'image', 'content')
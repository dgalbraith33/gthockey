from rest_framework import serializers
from gthockey.models import Player, Game, NewsStory, Board, Coach, ShopItem, Season


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name', 'position', 'number', 'hometown', 'school')


class GameMinSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    datetime = serializers.DateTimeField(read_only=True)
    opponent_name = serializers.CharField(read_only=True)
    rink_name = serializers.CharField(read_only=True)
    venue = serializers.CharField(read_only=True)

    is_reported = serializers.BooleanField(read_only=True)
    short_result = serializers.CharField(read_only=True)
    gt_score = serializers.IntegerField(read_only=True)
    opp_score = serializers.IntegerField(read_only=True)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'date', 'time', 'opponent', 'venue', 'location', 'season', 'score_gt_final',
                  'score_opp_final', 'short_result')
        depth = 1


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStory
        fields = ('id', 'title', 'date', 'image', 'content', 'teaser')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'first_name', 'last_name', 'position', 'email', 'image', 'description')


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'first_name', 'last_name', 'coach_position', 'email', 'image', 'bio')


class ShopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopItem
        fields = ('id', 'name', 'price', 'description', 'image', 'images', 'options',
                  'custom_options', 'in_stock')
        depth = 1


class ShopItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopItem
        fields = ('id', 'name', 'price', 'description', 'image')


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('id', 'name', 'year')

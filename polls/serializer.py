from rest_framework import serializers
from .models import Poll,PollHaveOptions,PollTable,Vote

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class PollHaveOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollHaveOptions
        fields = '__all__'

class PollTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollTable
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
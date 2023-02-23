from rest_framework import serializers

from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.ReadOnlyField(source='get_answer')

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['author', ]




class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['author', 'question']



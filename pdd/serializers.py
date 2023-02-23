from rest_framework import serializers

from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text', 'answer', 'id']
        read_only_fields = ['author', 'question']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source='question', many=True)

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['author', ]





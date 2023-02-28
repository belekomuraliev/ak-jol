from rest_framework import serializers

from .models import Question, Answer, Blog


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['author', 'question']


class QuestionSerializerAnswer(serializers.ModelSerializer):
    answers = AnswerSerializer(source='question', many=True)

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['author', ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['author', ]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['author', ]








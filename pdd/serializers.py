from rest_framework import serializers

from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ['author', 'question']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(source='question', many=True)

    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['author', 'questionNamber', 'description']

    def create(self, validated_data):
        description = Question.objects.create(
            description=validated_data['text'],
        )
        return description




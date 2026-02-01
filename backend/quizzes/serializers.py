from rest_framework import serializers
from .models import Quiz, Question, Choice, QuizAttempt

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'choices']


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='question_set', many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'questions']


class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = '__all__'

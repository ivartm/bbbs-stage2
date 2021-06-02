from rest_framework import generics

from bbbs.questions.models import Question
from bbbs.questions.serializers import QuestionSerializer


class QuestiosList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

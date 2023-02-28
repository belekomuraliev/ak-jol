from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,  get_object_or_404

from .models import Question, Answer, Blog
from .permissions import IsAdminOrReadOnly
from .serializers import QuestionSerializer, AnswerSerializer, QuestionSerializerAnswer, BlogSerializer


class QuestionListCrateAPIViewAnswer(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializerAnswer
    permission_classes = [IsAdminOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
        )


class QuestionListCrateAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
        )


class QuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly, ]

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))


class AnswerCreateAPIView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminOrReadOnly, ]

    def get_queryset(self):
        return super().get_queryset().filter(question_id=self.kwargs.get('question_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            question_id=self.kwargs.get('question_id'),
        )


class AnswerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminOrReadOnly, ]

    def get_object(self):
        return get_object_or_404(Answer, pk=self.kwargs.get('answer_id'))


class BlogListCreateAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer






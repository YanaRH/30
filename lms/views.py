from rest_framework import viewsets, permissions
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer



class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        # Фильтруем курсы текущего пользователя
        return Course.objects.filter(owner=self.request.user)
    
    
    
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        # Фильтруем уроки текущего пользователя
        return Lesson.objects.filter(owner=self.request.user)


class UserViewSet:
    pass
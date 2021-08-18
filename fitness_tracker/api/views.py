import datetime

import requests
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import permissions, status, response, viewsets, exceptions, decorators

from .serializers import UserActivSerializer, CreateActivSerializer
from .models import UserActivity


class UserActiveViewSet(viewsets.ModelViewSet):
    """Вьюсет для создания и получения информации об активности пользователя"""
    queryset = UserActivity.objects.select_related('user').all()
    serializer_class = UserActivSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # собственно поставил вьюсэт и заблокировал update, delete чтоб в дальнейшем на него расширять функцияонал
        # и не пришлось еще миксины подставлять
        if self.action in ('list', 'retrieve', 'create',):
            return UserActivity.objects.select_related('user').filter(user=self.request.user)
        else:
            raise exceptions.ValidationError('no method')

    def get_serializer_class(self):
        if self.action in ('create',):
            return CreateActivSerializer
        return UserActivSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def requests_per_day_or_hour(self, hour=False, day=False):
        # Оставил тут для наглядности. Такая логика обычно отдельно выносится.
        # Возможно не совсем понял постановку задачи поэтому сделал так
        start_datetime = datetime.datetime.now()
        finish_datetime = datetime.datetime.now()
        if hour and day:
            raise exceptions.ValidationError('обработка одновременно по дням и часам... нельзя так')
        elif day:
            start_datetime = finish_datetime - datetime.timedelta(hours=1)
        elif hour:
            start_datetime = finish_datetime - datetime.timedelta(days=1)
        active_user_ago = UserActivity.objects.filter(start_of_activity__range=(start_datetime, finish_datetime),
                                                      user=self.request.user)
        return UserActivSerializer(active_user_ago, many=True)

    @decorators.action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def activity_per_hour(self, request):
        serializer = self.requests_per_day_or_hour(hour=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @decorators.action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def activity_per_day(self, request):
        serializer = self.requests_per_day_or_hour(day=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    @decorators.action(detail=False, permission_classes=[permissions.AllowAny])
    def activate_user(self, request):
        # Сделал интереса ради. Чтоб просто юзер кликал по ссылке и дальше можно было спокойно логиниться
        try:
            uid = request.GET['uid']
            token = request.GET['token']
            requests.post(url='http://127.0.0.1:8000/auth/users/activation/', data={'uid': uid, 'token': token, })
            return response.Response(data='OK', status=status.HTTP_200_OK)
        except MultiValueDictKeyError:
            return response.Response(data='no token or uid', status=status.HTTP_400_BAD_REQUEST)

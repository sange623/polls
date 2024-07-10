from rest_framework import viewsets
from .models import Poll,PollHaveOptions,PollTable,Vote
from .serializer import PollSerializer,PollHaveOptionsSerializer,PollTableSerializer,VoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class PollViewset(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    search_fields = ['id' 'name']

class PollHaveOptionViewset(viewsets.ModelViewSet):
    queryset = PollHaveOptions.objects.all()
    serializer_class = PollHaveOptionsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    search_fields = ['id' 'name']

class PollTableViewset(viewsets.ModelViewSet):
    queryset = PollTable.objects.all()
    serializer_class = PollTableSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    search_fields = ['id' 'name']

class VoteViewset(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    search_fields = ['id' 'name']
    
    

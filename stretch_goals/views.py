from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from stretch_goals.models import User, Goal, Record
from stretch_goals.forms import GoalForm, RecordForm
from stretch_goals.serializers import UserSerializer, GoalSerializer, RecordSerializer

from rest_framework import viewsets, status, mixins, generics
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def home(request):
    goals = Goal.objects.all()
    form = RecordForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid:
            record = form.save(commit=False)
            record.user = request.user
            # record.goal = 
            record.save()
            return redirect(to='home')
        else:
            form = GoalForm(instance=request.user)
    return render(request, "stretch_goals/home.html", {'goals': goals, 'form': form})

def create_new_goal(request):
    form = GoalForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid:
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect(to='home')
        else:
            form = GoalForm(instance=request.user)

    return render(request, 'stretch_goals/create_new_goal.html', {"form": form})

# def create_new_record(request):
#     form = RecordForm(data=request.POST)
#     if request.method == 'POST':
#         if form.is_valid:
#             record = form.save(commit=False)
#             record.user = request.user
#             record.save()
#             return redirect(to='home', pk=goal.pk)
#         else:
#             form = GoalForm(instance=request.user)

#     return render(request, 'stretch_goals/home.html', {"form": form})

class GoalsList(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def goals_list(request, format=None):
#     if request.method == 'GET':
#         goals = Goal.objects.all()
#         serializer = GoalSerializer(goals, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = GoalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def goal_detail(request, pk, format=None):
#     try:
#         goal = Goal.objects.get(pk=pk)
#     except Goal.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = GoalSerializer(goal)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         serializer = GoalSerializer(goal, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         goal.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
 
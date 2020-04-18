from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from api.serializers import CompanySerializer,VacancySerializer
from rest_framework.decorators import api_view

from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.
from api.models import Company, Vacancy


@api_view(['GET', 'POST'])
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.order_by('id')
        serializer = CompanySerializer(companies, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error':serializer.errors})


@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Exception as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
def vacancies(request, company_id):
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id=company_id)
        serializer = VacancySerializer(vacancies, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Exception as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse({'error': serializer.errors})

    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({"deleted":True})


@api_view(['GET', 'PUT'])
def all_vacancies_top10(request):
    vacancies = Vacancy.objects.all().order_by('-salary')
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
def company_vacancies_top10(request, company_id):
    vacancies = Vacancy.objects.all().filter(company_id=company_id).order_by('-salary')
    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data)

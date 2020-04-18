from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Company, Vacancy

from api.serializers import CompanySerializer, VacancySerializer

class CompaniesAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyDetailView(APIView):
    def get_company(self, company_id):
        try:
            return Company.objects.get(id=company_id)
        except Exception as e:
            return Response({'error': str(e)})

    def get(self,request, company_id):
        company = self.get_company(company_id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    def put(self, request, company_id):
        company = self.get_company(company_id)
        serializer = CompanySerializer(instance=company, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, company_id):
        company = self.get_company(company_id)
        company.delete()
        return Response({'deleted':True})



class VacanciesAPIView(APIView):
    def get_vacancies(self, company_id):
        try:
            return Vacancy.objects.filter(company_id=company_id)
        except Exception as e:
            return Response({'error': str(e)})

    def get(self, request, company_id):
        vacancies = self.get_vacancies(company_id)
        serializer = VacancySerializer(vacancies, many = True)
        return Response(serializer.data)

    def post(self,request, company_id):
        serializer = VacancySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework import generics
from rest_framework import mixins
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer,CompanyWithVacanciesSerializer
from rest_framework.permissions import IsAuthenticated


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyWithVacanciesSerializer
    permission_classes = (IsAuthenticated,)


class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    lookup_url_kwarg = 'company_id'
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)


class VacancyListAPIView(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                          generics.GenericAPIView):

    queryset = Vacancy.objects.all()
    lookup_url_kwarg = 'company_id'
    serializer_class = VacancySerializer

    def get_vacancies(self,company_id):
        try:
            return Vacancy.objects.filter(company_id=company_id)
        except Exception as e:
            return print({'error': str(e)})

    def get(self, request, *args, **kwargs):
        company_id = kwargs.get('company_id')
        self.queryset = self.get_vacancies(company_id)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    permission_classes = (IsAuthenticated,)


class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    lookup_url_kwarg = 'vacancy_id'
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated,)

from django.urls import path
from django.views.generic import RedirectView
from api.views import companies, company_detail, vacancies, vacancy_detail, all_vacancies_top10, company_vacancies_top10
from api.views.views_cbv import CompaniesAPIView, CompanyDetailView, VacanciesAPIView
from api.views.views_generic import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('api/login/',obtain_jwt_token),
    path('api/companies/', CompanyListAPIView.as_view(), name="companies"),
    path('api/companies/<int:company_id>/', CompanyDetailAPIView.as_view(), name="company_detail"),
    path('api/companies/<int:company_id>/vacancies/', VacancyListAPIView.as_view(), name="vacancies"),
    path('api/vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view(), name="vacancy_detail"),
    path('api/vacancies/top_ten', all_vacancies_top10, name="vacancies_top10"),
    path('api/<int:company_id>/vacancies/top_ten', company_vacancies_top10, name="comp_vacancies_top10")
]

from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from api.models import Company, Vacancy


@csrf_exempt
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.order_by('id')
        company_list = [company.short() for company in companies]
        return JsonResponse(company_list, safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)
        company = Company.objects.create(name=request_body.get('name', 'Default Company name'),
                                         description=request_body.get('description', 'No description'),
                                         city=request_body.get('city', 'No city'),
                                         address=request_body.get('address', 'No address'))
        return JsonResponse(company.short())


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Exception as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(company.short())
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        company.name = request_body.get('name', company.name)
        company.description = request_body.get('description', company.description)
        company.city = request_body.get('city', company.city)
        company.address = request_body.get('address', company.address)
        company.save()
        return JsonResponse(company.short())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
def vacancies(request, company_id):
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id=company_id)
        vacancy_list = [vacancy.short() for vacancy in vacancies]
        return JsonResponse(vacancy_list, safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)
        vacancy = Vacancy.objects.create(name=request_body.get('name', 'Unknown'),
                                         description= request_body.get('description', 'No description'),
                                         salary=request_body.get('salary', 'No salary'),
                                         company_id = company_id)
        return JsonResponse(vacancy.short(), safe = False)

@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Exception as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(vacancy.short())
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        vacancy.name = request_body.get('name', vacancy.name)
        vacancy.description = request_body.get('description', vacancy.description)
        vacancy.salary = request_body.get('salary', vacancy.salary)
        vacancy.save()
        return JsonResponse(vacancy.short())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({"deleted":True})



def all_vacancies_top10(request):
    vacancies = Vacancy.objects.all().order_by('-salary')
    top_vacancy_list = [vacancy.short() for vacancy in vacancies[:10]]
    return JsonResponse(top_vacancy_list, safe=False)


def company_vacancies_top10(request, company_id):
    vacancies = Vacancy.objects.all().filter(company_id=company_id).order_by('-salary')
    top_vacancy_list = [vacancy.short() for vacancy in vacancies[:10]]
    return JsonResponse(top_vacancy_list, safe=False)

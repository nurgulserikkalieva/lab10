import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Company} from './company';
import {Vacancy} from './vacancy';

export class LoginResponse {
  token: string;
}

export class DeleteResponse{
  deleted:Boolean;
}

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  companyID:number = 0
  vacancyID:number = 0

  BASE_URL = 'http://127.0.0.1:8000';
  constructor(private http: HttpClient) {}

  getCompanyList(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.BASE_URL}/api/companies/`);
  }

  getCompany(id): Observable<Company> {
    return this.http.get<Company>(`${this.BASE_URL}/api/companies/${id}/`);
  }

  deleteCompany(id): Observable<any> {
    return this.http.delete(`${this.BASE_URL}/api/companies/${id}/`);
  }

  getVacancyList(id): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.BASE_URL}/api/companies/${id}/vacancies/`);
  }

  getVacancy(id): Observable<Vacancy> {
    return this.http.get<Vacancy>(`${this.BASE_URL}/api/vacancies/${id}/`);
  }

  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/api/login/`, {
      username,
      password
    });
  }

  addCompany(name, description,city,address): Observable<Company>{
    return this.http.post<Company>(`${this.BASE_URL}/api/companies/`,{
      name,
      description,
      city,
      address
    });
  }


  addVacancy(name, description, salary, company):Observable<Vacancy>{
    return this.http.post<Vacancy>(`${this.BASE_URL}/api/companies/${company}/vacancies/`,{
      name,
      description,
      salary,
      company
    });
  }


  deleteVacancy(vacancy){
    const id = vacancy.id;
    return this.http.delete<DeleteResponse>(`${this.BASE_URL}/api/vacancies/${id}/`)
  }
}
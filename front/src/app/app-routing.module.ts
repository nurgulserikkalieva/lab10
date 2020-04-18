import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompaniesComponent} from './companies/companies.component';
import {VacanciesComponent} from './vacancies/vacancies.component';
import { CompanyDetailsComponent } from './company-details/company-details.component';
import {VavancyDetailsComponent} from './vavancy-details/vavancy-details.component'

const routes: Routes = [
  { path: '', component: CompaniesComponent },
  { path: 'companies/:id/vacancies', component: VacanciesComponent },
  { path: 'companies/:id', component: CompanyDetailsComponent },
  { path: 'vacancies/:id', component: VavancyDetailsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
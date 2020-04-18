import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppComponent} from './app.component';
import {CompaniesComponent} from './companies/companies.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {AuthInterceptor} from './auth.interceptor';
import {RouterModule} from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { VacanciesComponent } from './vacancies/vacancies.component';
import {FormsModule} from '@angular/forms';
import { CompanyDetailsComponent } from './company-details/company-details.component';
import { VavancyDetailsComponent } from './vavancy-details/vavancy-details.component';

@NgModule({
  declarations: [
    AppComponent,
    CompaniesComponent,
    VacanciesComponent,
    CompanyDetailsComponent,
    VavancyDetailsComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
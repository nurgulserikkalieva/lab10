import {Component, OnInit, Input} from '@angular/core';
import {Company} from '../company';
import {CompanyService} from '../company.service';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {
  companies: Company[];

  @Input() name:string;
  @Input() description:string;
  @Input() city:string;
  @Input() address:string;

  constructor(private companyService: CompanyService) {
  }

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies() {
    this.companyService.getCompanyList()
      .subscribe(companies => {
        this.companies = companies;
      });
  }

  addCompany(){
    window.alert(this.description)
    this.companyService.addCompany(this.name, this.description,this.city, this.address)
      .subscribe(company => {
        this.companies.push(company)
      })
  }
}
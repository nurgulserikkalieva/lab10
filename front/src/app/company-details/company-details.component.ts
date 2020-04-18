import { Component, OnInit } from '@angular/core';
import {CompanyService} from '../company.service'
import {Company} from '../company'
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-company-details',
  templateUrl: './company-details.component.html',
  styleUrls: ['./company-details.component.css']
})
export class CompanyDetailsComponent implements OnInit {

  company:Company
  id:string


  constructor(private companyService:CompanyService,
              public route:ActivatedRoute) { }

  ngOnInit(): void {
    this.getCompany()
  }


  delete(id){
    window.alert("This company was deleted!")
    this.companyService.deleteCompany(id).subscribe()
  }


  getCompany(){
    this.id = this.route.snapshot.paramMap.get('id');
    this.id = this.id.substr(1);
    this.companyService.getCompany(this.id)
      .subscribe(company=>{
        this.company = company
      })
    }
}

import { Component, OnInit } from '@angular/core';
import {CompanyService} from '../company.service';
import {ActivatedRoute} from '@angular/router';
import {Vacancy} from '../vacancy'

@Component({
  selector: 'app-vavancy-details',
  templateUrl: './vavancy-details.component.html',
  styleUrls: ['./vavancy-details.component.css']
})
export class VavancyDetailsComponent implements OnInit {

  id:string
  vacancy:Vacancy

  constructor(private companyService:CompanyService, public route:ActivatedRoute) { 
    this.getVacancy()
  }

  getVacancy(){
    this.id = this.route.snapshot.paramMap.get('id');
    this.id = this.id.substr(1);
    this.companyService.getVacancy(this.id)
      .subscribe(vacancy=>{
        this.vacancy = vacancy
      })
  }

  ngOnInit(): void {
  }

}

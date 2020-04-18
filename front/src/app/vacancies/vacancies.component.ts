import {Component, OnInit, Input} from '@angular/core';
import {Vacancy} from '../vacancy';
import {CompanyService} from '../company.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {

  vacancies: Vacancy[];

  compId:number
  @Input() name:string;
  @Input() description: string;
  @Input() salary: number;

  constructor(private companyService: CompanyService,
              public route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.getVacanciesList();
  }

  addVacancy(){
    window.alert(parseInt(this.compId.toString()))
    this.companyService.addVacancy(this.name, this.description, this.salary, this.compId)
      .subscribe(vacancy => {
        this.vacancies.push(vacancy)
      })

      this.name = ''
      this.description = ''
      this.salary = null
  }

  deleteVacancy(vacancy:Vacancy){
    window.alert("This vacancy was deleted!")
    this.vacancies = this.vacancies.filter(v=>v!=vacancy)
    this.companyService.deleteVacancy(vacancy).subscribe()
  }

  getVacanciesList() {
    let id = this.route.snapshot.paramMap.get('id');
    id = id.substr(1);
    this.compId = parseInt(id)
    this.companyService.getVacancyList(id)
      .subscribe(vacancies => {
        this.vacancies = vacancies;
      });
  }

}
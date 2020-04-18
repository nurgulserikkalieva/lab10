import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VavancyDetailsComponent } from './vavancy-details.component';

describe('VavancyDetailsComponent', () => {
  let component: VavancyDetailsComponent;
  let fixture: ComponentFixture<VavancyDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VavancyDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VavancyDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

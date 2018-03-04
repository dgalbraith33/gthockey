import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SidebarRecordComponent } from './sidebar-record.component';

describe('SidebarRecordComponent', () => {
  let component: SidebarRecordComponent;
  let fixture: ComponentFixture<SidebarRecordComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SidebarRecordComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SidebarRecordComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

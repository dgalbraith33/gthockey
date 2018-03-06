import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SidebarCountdownComponent } from './sidebar-countdown.component';

describe('SidebarCountdownComponent', () => {
  let component: SidebarCountdownComponent;
  let fixture: ComponentFixture<SidebarCountdownComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SidebarCountdownComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SidebarCountdownComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

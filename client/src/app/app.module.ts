import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { RecaptchaModule } from 'ng-recaptcha';
import { RecaptchaFormsModule } from 'ng-recaptcha/forms';


import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { ApiService } from './api/api.service';
import { ContactFormComponent } from './forms/contact-form/contact-form.component';
import { ProspectFormComponent } from './forms/prospect-form/prospect-form.component';
import { ArticleComponent } from './pages/article/article.component';
import { FrontpageComponent } from './pages/frontpage/frontpage.component';
import { InvolvementComponent } from './pages/involvement/involvement.component';
import { LeadershipComponent } from './pages/leadership/leadership.component';
import { RosterComponent } from './pages/roster/roster.component';
import { ScheduleComponent } from './pages/schedule/schedule.component';
import { SidebarCountdownComponent } from './sidebar/sidebar-countdown/sidebar-countdown.component';
import { SidebarRecordComponent } from './sidebar/sidebar-record/sidebar-record.component';


@NgModule({
  declarations: [
    AppComponent,
    ArticleComponent,
    ContactFormComponent,
    FrontpageComponent,
    InvolvementComponent,
    LeadershipComponent,
    ProspectFormComponent,
    RosterComponent,
    ScheduleComponent,
    SidebarRecordComponent,
    SidebarCountdownComponent,
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RecaptchaFormsModule,
    RecaptchaModule.forRoot(),
  ],
  providers: [
    ApiService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

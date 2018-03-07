import { SidebarRecordComponent } from './sidebar/sidebar-record.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RecaptchaModule } from 'ng-recaptcha';
import { RecaptchaFormsModule } from 'ng-recaptcha/forms';


import { AppComponent } from './app.component';
import { ApiService } from './api.service';
import { RosterComponent } from './roster/roster.component';
import { AppRoutingModule } from './/app-routing.module';
import { FrontpageComponent } from './frontpage/frontpage.component';
import { ScheduleComponent } from './schedule/schedule.component';
import { LeadershipComponent } from './leadership/leadership.component';
import { SidebarCountdownComponent } from './sidebar/sidebar-countdown/sidebar-countdown.component';
import { ArticleComponent } from './article/article.component';
import { ContactFormComponent } from './contact-form/contact-form.component';


@NgModule({
  declarations: [
    AppComponent,
    RosterComponent,
    FrontpageComponent,
    ScheduleComponent,
    SidebarRecordComponent,
    LeadershipComponent,
    SidebarCountdownComponent,
    ArticleComponent,
    ContactFormComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    RecaptchaModule.forRoot(),
    RecaptchaFormsModule,
  ],
  providers: [
    ApiService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

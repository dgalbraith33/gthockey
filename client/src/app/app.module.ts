import { SidebarRecordComponent } from './sidebar/sidebar-record.component';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';


import { AppComponent } from './app.component';
import { ApiService } from './api.service';
import { RosterComponent } from './roster/roster.component';
import { AppRoutingModule } from './/app-routing.module';
import { FrontpageComponent } from './frontpage/frontpage.component';
import { ScheduleComponent } from './schedule/schedule.component';
import { LeadershipComponent } from './leadership/leadership.component';
import { SidebarCountdownComponent } from './sidebar/sidebar-countdown/sidebar-countdown.component';
import { ArticleComponent } from './article/article.component';


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
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
  ],
  providers: [
    ApiService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

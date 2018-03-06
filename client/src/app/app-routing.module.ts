import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ArticleComponent } from './article/article.component';
import { FrontpageComponent } from './frontpage/frontpage.component';
import { LeadershipComponent } from './leadership/leadership.component';
import { RosterComponent } from './roster/roster.component';
import { ScheduleComponent } from './schedule/schedule.component';

const routes: Routes = [
  { path: '', component: FrontpageComponent},
  { path: 'roster', component: RosterComponent },
  { path: 'schedule', component: ScheduleComponent},
  { path: 'board', component: LeadershipComponent},
  { path: 'article/:id', component: ArticleComponent},
];


@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ],
})
export class AppRoutingModule { }

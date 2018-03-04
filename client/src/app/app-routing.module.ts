import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { FrontpageComponent } from './frontpage/frontpage.component';
import { RosterComponent } from './roster/roster.component';

const routes: Routes = [
  { path: '', component: FrontpageComponent},
  { path: 'roster', component: RosterComponent }
];


@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ],
})
export class AppRoutingModule { }

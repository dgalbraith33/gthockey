import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { RosterComponent } from './roster/roster.component'

const routes: Routes = [
  { path: '', redirectTo: '', pathMatch: 'full'},
  { path: 'roster', component: RosterComponent }
];


@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ],
})
export class AppRoutingModule { }

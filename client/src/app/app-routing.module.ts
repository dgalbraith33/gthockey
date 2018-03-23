import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ContactFormComponent } from './forms/contact-form/contact-form.component';
import { ProspectFormComponent } from './forms/prospect-form/prospect-form.component';
import { ArticleComponent } from './pages/article/article.component';
import { CartComponent } from './pages/cart/cart.component';
import { FrontpageComponent } from './pages/frontpage/frontpage.component';
import { InvolvementComponent } from './pages/involvement/involvement.component';
import { LeadershipComponent } from './pages/leadership/leadership.component';
import { RosterComponent } from './pages/roster/roster.component';
import { ScheduleComponent } from './pages/schedule/schedule.component';
import { ShopComponent } from './pages/shop/shop.component';
import { ShopItemComponent } from './pages/shop-item/shop-item.component';

const routes: Routes = [
  { path: '', component: FrontpageComponent},
  { path: 'roster', component: RosterComponent },
  { path: 'schedule', component: ScheduleComponent},
  { path: 'board', component: LeadershipComponent},
  { path: 'article/:id', component: ArticleComponent},
  { path: 'contact', component: ContactFormComponent},
  { path: 'prospect', component: ProspectFormComponent},
  { path: 'involvement', component: InvolvementComponent},
  { path: 'shop', component: ShopComponent },
  { path: 'shop/:id', component: ShopItemComponent },
  { path: 'cart', component: CartComponent },
];


@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ],
})
export class AppRoutingModule { }

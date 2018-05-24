import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { Angulartics2Module } from 'angulartics2';
import { Angulartics2GoogleAnalytics } from 'angulartics2/ga';
import { RecaptchaModule } from 'ng-recaptcha';
import { RecaptchaFormsModule } from 'ng-recaptcha/forms';


import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { ApiService } from './api/api.service';
import { CartService } from './cart/cart.service';
import { ItemFormComponent } from './forms/item-form/item-form.component';
import { CartFormComponent } from './forms/cart-form/cart-form.component';
import { ContactFormComponent } from './forms/contact-form/contact-form.component';
import { OrderFormComponent } from './forms/order-form/order-form.component';
import { ProspectFormComponent } from './forms/prospect-form/prospect-form.component';
import { ArticleComponent } from './pages/article/article.component';
import { CartComponent } from './pages/cart/cart.component';
import { FrontpageComponent } from './pages/frontpage/frontpage.component';
import { InvolvementComponent } from './pages/involvement/involvement.component';
import { LeadershipComponent } from './pages/leadership/leadership.component';
import { RosterComponent } from './pages/roster/roster.component';
import { ScheduleComponent } from './pages/schedule/schedule.component';
import { SidebarCountdownComponent } from './sidebar/sidebar-countdown/sidebar-countdown.component';
import { SidebarRecordComponent } from './sidebar/sidebar-record/sidebar-record.component';
import { ShopComponent } from './pages/shop/shop.component';
import { ShopItemComponent } from './pages/shop-item/shop-item.component';
import { CarouselComponent } from './common/carousel/carousel.component';
import { PaypalButtonComponent } from './forms/paypal-button/paypal-button.component';



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
    ShopComponent,
    ShopItemComponent,
    ItemFormComponent,
    CartFormComponent,
    OrderFormComponent,
    CartComponent,
    CarouselComponent,
    PaypalButtonComponent,
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RecaptchaFormsModule,
    RecaptchaModule.forRoot(),
    Angulartics2Module.forRoot([Angulartics2GoogleAnalytics]),
  ],
  providers: [
    ApiService,
    CartService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

import { Component, OnInit, ViewChild } from '@angular/core';


import { environment } from '../../../environments/environment';
import { ApiService } from '../../api/api.service';
import { Order } from '../../api/order';
import { CartService } from '../../cart/cart.service';
import { RecaptchaComponent } from 'ng-recaptcha';

@Component({
  selector: 'app-order-form',
  templateUrl: './order-form.component.html',
  styleUrls: ['./order-form.component.css']
})
export class OrderFormComponent implements OnInit {

  model = new Order();

  success: boolean;
  errors: any = {};

  readonly recaptchaKey = environment.recaptchaKey;
  @ViewChild(RecaptchaComponent) recaptcha: RecaptchaComponent;

  constructor(readonly cartService: CartService,
              private apiService: ApiService) { }

  ngOnInit() {
  }

  submitForm() {
    this.model.items = this.cartService.allItems();
    this.apiService.postOrderForm(this.model).subscribe(response => {
      this.success = true;
      this.errors = {};
      this.recaptcha.reset();
      this.model = new Order();
    }, response => {
      this.success = false;
      this.errors = response.error.errors;
      this.recaptcha.reset();
    });
  }
}

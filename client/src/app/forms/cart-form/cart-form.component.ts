import { Component, OnInit } from '@angular/core';

import { CartService } from '../../cart/cart.service';

@Component({
  selector: 'app-cart-form',
  templateUrl: './cart-form.component.html',
  styleUrls: ['./cart-form.component.css']
})
export class CartFormComponent implements OnInit {

  constructor(readonly cartService: CartService) { }

  ngOnInit() {
  }

  submitForm() {
  }

}

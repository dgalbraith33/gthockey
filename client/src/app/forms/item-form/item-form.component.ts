import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import {first} from 'rxjs/operators';

import { ApiService } from '../../api/api.service';
import { CartItem } from '../../api/cart-item';
import { ShopItem } from '../../api/shop-item';
import { CartService } from '../../cart/cart.service';

@Component({
  selector: 'app-item-form',
  templateUrl: './item-form.component.html',
  styleUrls: ['./item-form.component.css']
})
export class ItemFormComponent implements OnInit {

  private id: number;
  private item: ShopItem;
  model: CartItem;

  success: boolean;
  errors: any;
  option_unselected: any = {};

  constructor(private route: ActivatedRoute,
              private apiService: ApiService,
              private cartService: CartService) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get('id'), 10);
    this.getItem();
  }

  private getItem() {
    this.apiService.getShopItem(this.id).pipe(first()).subscribe(item => {
      this.item = item;
      this.model = new CartItem(item);
    });
  }

  submitForm() {
    let valid = true;
    for (const optionlist of this.item.options) {
      if (!this.model.options[optionlist.id]) {
        valid = false;
        this.option_unselected[optionlist.id] = true;
      } else {
        this.option_unselected[optionlist.id] = false;
      }
    }
    if (valid) {
      this.cartService.addItem(this.model);
      this.success = true;
      this.model = new CartItem(this.item);
    }
  }

  getOptions(option_str: string): string[] {
    return option_str.split(',');
  }

}

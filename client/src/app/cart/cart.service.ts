import { Injectable } from '@angular/core';

import { CartItem } from '../api/cart-item';
import { ShopItem } from '../api/shop-item';

@Injectable()
export class CartService {

  private items: CartItem[] = [];

  constructor() {
  }

  addItem(item: CartItem) {
    this.items.push(item);
  }

  empty(): boolean {
    return this.items.length === 0;
  }

  allItems(): CartItem[] {
    return this.items;
  }

  removeItem(index: number) {
    this.items.splice(index, 1);
  }

  totalCost(): number {
    let sum = 0;
    for (const item of this.items) {
      sum += this.getPrice(item);
    }
    return sum;
  }

  reset() {
    this.items = [];
  }

  private getPrice(item: CartItem): number {
    let price = item.shopItem.price;
    if (item.shopItem && item.shopItem.custom_options) {
      for (const option of item.shopItem.custom_options) {
        if (option.extra_cost && item.custom_options[option.id]) {
          price += option.extra_cost;
        }
      }
    }
    return price;
  }
}

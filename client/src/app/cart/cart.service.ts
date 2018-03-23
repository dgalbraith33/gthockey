import { Injectable } from '@angular/core';

import { CartItem } from '../api/cart-item';

@Injectable()
export class CartService {

  private items: CartItem[] = [];

  constructor() { }

  addItem(item: CartItem) {
    this.items.push(item);
    console.log(this.items);
  }

  empty(): boolean {
    return this.items.length === 0;
  }

  allItems(): CartItem[] {
    return this.items;
  }
}

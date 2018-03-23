import { Component, OnInit } from '@angular/core';

import { ApiService } from '../../api/api.service';
import { ShopItem } from '../../api/shop-item';

@Component({
  selector: 'app-shop',
  templateUrl: './shop.component.html',
  styleUrls: ['./shop.component.css']
})
export class ShopComponent implements OnInit {

  items: ShopItem[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getItems();
  }

  private getItems() {
    this.apiService.getShopItems().subscribe(items => this.items = items);
  }

}

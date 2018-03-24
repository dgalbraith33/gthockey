import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { ApiService } from '../../api/api.service';
import { ShopItem } from '../../api/shop-item';
import { CarouselItem } from '../../common/carousel/carousel';

@Component({
  selector: 'app-shop-item',
  templateUrl: './shop-item.component.html',
  styleUrls: ['./shop-item.component.css']
})
export class ShopItemComponent implements OnInit {

  private id: number;
  item: ShopItem;
  imageCarousel: CarouselItem[];

  constructor(private route: ActivatedRoute,
              private apiService: ApiService) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get('id'), 10);
    this.getItem();
  }

  private getItem() {
    this.apiService.getShopItem(this.id).subscribe(item => {
      this.item = item;
      this.imageCarousel = [];
      this.imageCarousel.push(new CarouselItem(item.image));
      item.images.forEach(image => {
        this.imageCarousel.push(new CarouselItem(image.image));
      });
    });
  }

  paragraphs(description: string): string[] {
    return description.split('\n');
  }

}

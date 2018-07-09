import { Component, OnInit } from '@angular/core';

import { ApiService } from './../../api/api.service';
import { Article } from '../../api/article';
import { GameMin } from '../../api/game';
import { CarouselItem } from '../../common/carousel/carousel';

@Component({
  selector: 'app-frontpage',
  templateUrl: './frontpage.component.html',
  styleUrls: ['./frontpage.component.css']
})
export class FrontpageComponent implements OnInit {

  carouselItems: CarouselItem[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getArticles();
  }

  private getArticles() {
    this.apiService.getArticles().subscribe(articles => {
      const tempItems: CarouselItem[] = [];
      articles.forEach(article => {
        const item = new CarouselItem();
        item.image = article.image;
        item.text = article.title;
        item.route = '/article/' + article.id;
        tempItems.push(item);
      });
      this.carouselItems = tempItems;
    });
  }

}

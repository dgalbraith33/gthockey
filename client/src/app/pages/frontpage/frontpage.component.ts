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
  recentGames: GameMin[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getArticles();
    this.getGames();
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

  private getGames() {
    this.apiService.getGames({limit: 5, date_to: this.getYesterday(), desc: true}).subscribe(games => this.recentGames = games);
  }

  private getYesterday(): string {
    const date = new Date();
    date.setDate(date.getDate() - 1);
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
  }

}

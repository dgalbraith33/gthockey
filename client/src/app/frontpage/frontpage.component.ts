import { Component, OnInit } from '@angular/core';

import { ApiService } from './../api.service';
import { Article } from '../api/article';
import { GameMin } from '../api/game';

@Component({
  selector: 'app-frontpage',
  templateUrl: './frontpage.component.html',
  styleUrls: ['./frontpage.component.css']
})
export class FrontpageComponent implements OnInit {

  private articles: Article[];
  private recentGames: GameMin[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getArticles();
    this.getGames();
  }

  private getArticles() {
    this.apiService.getArticles().subscribe(articles => this.articles = articles);
  }

  private getGames() {
    this.apiService.getGames({limit: 5, date_to: this.getYesterday(), desc: true}).subscribe(games => this.getRecent(games));
  }

  private getYesterday(): string {
    const date = new Date();
    date.setDate(date.getDate() - 1);
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
  }

  private getRecent(games: GameMin[]) {
    this.recentGames = [];
    let index = games.length - 1;
    const today = new Date();
    while (this.recentGames.length < 5 && index >= 0) {
      if (new Date(games[index].date) < today) {
        this.recentGames.push(games[index]);
      }
      index--;
    }
  }

}

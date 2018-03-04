import { Component, OnInit } from '@angular/core';

import { ApiService } from './../api.service';
import { Article } from '../api/article';
import { Game } from '../api/game';

@Component({
  selector: 'app-frontpage',
  templateUrl: './frontpage.component.html',
  styleUrls: ['./frontpage.component.css']
})
export class FrontpageComponent implements OnInit {

  private articles: Article[];
  private recentGames: Game[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getArticles();
    this.getGames();
  }

  private getArticles() {
    this.apiService.getArticles().subscribe(articles => this.articles = articles);
  }

  private getGames() {
    this.apiService.getGames().subscribe(games => this.getRecent(games));
  }

  private getRecent(games: Game[]) {
    this.recentGames = [];
    console.log(games);
    console.log('processing');
    let index = games.length - 1;
    const today = new Date();
    console.log(today);
    while (this.recentGames.length < 5 && index >= 0) {
      if (new Date(games[index].date) < today) {
        console.log('found');
        this.recentGames.push(games[index]);
      }
      index--;
    }
  }

}

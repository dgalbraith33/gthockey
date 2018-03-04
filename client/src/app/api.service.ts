import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

import { Article } from './api/article';
import { Game } from './api/game';
import { Player } from './api/player';

@Injectable()
export class ApiService {

  private rosterUrl = '/api/players';
  private articleUrl = '/api/articles';
  private gameUrl = '/api/games';

  constructor(private http: HttpClient) { }

  getPlayers(): Observable<Player[]> {
    return this.http.get<Player[]>(this.rosterUrl);
  }

  getArticles(): Observable<Article[]> {
    return this.http.get<Article[]>(this.articleUrl);
  }

  getGames(): Observable<Game[]> {
    return this.http.get<Game[]>(this.gameUrl).map((games: Game[]) => games.map(game => new Game(game)));
  }
}

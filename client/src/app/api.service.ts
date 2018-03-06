import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

import { Article } from './api/article';
import { Board } from './api/board';
import { Coach } from './api/coach';
import { Game, GameMin } from './api/game';
import { Player } from './api/player';
import { environment } from './../environments/environment';

@Injectable()
export class ApiService {

  private rosterUrl = '/api/players/';
  private articleUrl = '/api/articles/';
  private gameUrl = '/api/games/';
  private boardUrl = '/api/board/';
  private coachUrl = '/api/coaches/';

  constructor(private http: HttpClient) { }

  getPlayers(): Observable<Player[]> {
    return this.http.get<Player[]>(this.getUrl(this.rosterUrl));
  }

  getArticles(): Observable<Article[]> {
    return this.http.get<Article[]>(this.getUrl(this.articleUrl));
  }

  getGames(params: any = {}): Observable<GameMin[]> {
    return this.http.get<GameMin[]>(this.getUrl(this.gameUrl), {params}).map((games: GameMin[]) => games.map(game => new GameMin(game)));
  }

  getGame(id: number): Observable<Game> {
    return this.http.get<Game>(this.getUrl(this.gameUrl) + id + '/');
  }

  getBoard(): Observable<Board[]> {
    return this.http.get<Board[]>(this.getUrl(this.boardUrl));
  }

  getCoaches(): Observable<Coach[]> {
    return this.http.get<Coach[]>(this.getUrl(this.coachUrl));
  }

  private getUrl(path: string) {
    return environment.apiurl + path;
  }
}

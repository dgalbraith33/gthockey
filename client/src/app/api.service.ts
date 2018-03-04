import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';

import { Article } from './api/article';
import { Player } from './api/player';

@Injectable()
export class ApiService {

  private rosterUrl = '/api/players';
  private articleUrl = '/api/articles';

  constructor(private http: HttpClient) { }

  getPlayers(): Observable<Player[]> {
    return this.http.get<Player[]>(this.rosterUrl);
  }

  getArticles(): Observable<Article[]> {
    return this.http.get<Article[]>(this.articleUrl);
  }
}

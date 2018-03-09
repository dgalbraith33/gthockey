import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

import { Article } from './api/article';
import { Board } from './api/board';
import { Coach } from './api/coach';
import { ContactForm } from './api/contact';
import { Game, GameMin } from './api/game';
import { Player } from './api/player';
import { ProspectForm } from './api/prospect';
import { environment } from './../environments/environment';
import { InvolvementForm } from './api/involvement';

@Injectable()
export class ApiService {

  private rosterUrl = '/api/players/';
  private articleUrl = '/api/articles/';
  private gameUrl = '/api/games/';
  private boardUrl = '/api/board/';
  private coachUrl = '/api/coaches/';

  private contactFormUrl = '/api/forms/contact/';
  private prospectFormUrl = '/api/forms/prospect/';
  private involvementFormUrl = '/api/forms/involvement/';

  constructor(private http: HttpClient) { }

  getPlayers(): Observable<Player[]> {
    return this.http.get<Player[]>(this.getUrl(this.rosterUrl));
  }

  getArticles(): Observable<Article[]> {
    return this.http.get<Article[]>(this.getUrl(this.articleUrl));
  }

  getArticle(id: number): Observable<Article> {
    return this.http.get<Article>(this.getUrl(this.articleUrl) + id + '/');
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

  postContactForm(form: ContactForm) {
    return this.http.post<any>(this.getUrl(this.contactFormUrl), this.toFormData(form));
  }

  postProspectForm(form: ProspectForm) {
    return this.http.post<any>(this.getUrl(this.prospectFormUrl), this.toFormData(form));
  }

  postInvolvementForm(form: InvolvementForm) {
    return this.http.post<any>(this.getUrl(this.involvementFormUrl), this.toFormData(form));
  }

  private getUrl(path: string) {
    return environment.apiurl + path;
  }

  private toFormData(form: any) {
    const data = new FormData();
    for (const key of Object.keys(form)) {
      data.append(key, form[key]);
    }
    return data;
  }
}

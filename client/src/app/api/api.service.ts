import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

import 'rxjs/add/operator/map';
import { Observable } from 'rxjs/Observable';

import { environment } from './../../environments/environment';
import { Article } from './article';
import { Board } from './board';
import { Coach } from './coach';
import { ContactForm } from './contact';
import { Game, GameMin } from './game';
import { InvolvementForm } from './involvement';
import { Player } from './player';
import { ProspectForm } from './prospect';

@Injectable()
export class ApiService {

  private readonly apiEndpoint: string;
  private readonly formEndpoint: string;

  private readonly rosterUrl: string;
  private readonly articleUrl: string;
  private readonly gameUrl: string;
  private readonly boardUrl: string;
  private readonly coachUrl: string;

  private readonly contactFormUrl: string;
  private readonly prospectFormUrl: string;
  private readonly involvementFormUrl: string;

  constructor(private http: HttpClient) {
    this.apiEndpoint = environment.apiurl + '/api/';
    this.formEndpoint = this.apiEndpoint + 'forms/';

    this.rosterUrl = this.apiEndpoint + 'players/';
    this.articleUrl = this.apiEndpoint + 'articles/';
    this.gameUrl = this.apiEndpoint +  'games/';
    this.boardUrl = this.apiEndpoint + 'board/';
    this.coachUrl = this.apiEndpoint + 'coaches/';

    this.contactFormUrl = this.formEndpoint + 'contact/';
    this.prospectFormUrl = this.formEndpoint + 'prospect/';
    this.involvementFormUrl = this.formEndpoint + 'involvement/';
   }

  getPlayers(): Observable<Player[]> {
    return this.http.get<Player[]>(this.rosterUrl);
  }

  getArticles(): Observable<Article[]> {
    return this.http.get<Article[]>(this.articleUrl);
  }

  getArticle(id: number): Observable<Article> {
    return this.http.get<Article>(this.articleUrl + id + '/');
  }

  getGames(params: any = {}): Observable<GameMin[]> {
    return this.http.get<GameMin[]>(this.gameUrl, {params}).map((games: GameMin[]) => games.map(game => new GameMin(game)));
  }

  getGame(id: number): Observable<Game> {
    return this.http.get<Game>(this.gameUrl + id + '/');
  }

  getBoard(): Observable<Board[]> {
    return this.http.get<Board[]>(this.boardUrl);
  }

  getCoaches(): Observable<Coach[]> {
    return this.http.get<Coach[]>(this.coachUrl);
  }

  postContactForm(form: ContactForm) {
    return this.http.post<any>(this.contactFormUrl, this.toFormData(form));
  }

  postProspectForm(form: ProspectForm) {
    return this.http.post<any>(this.prospectFormUrl, this.toFormData(form));
  }

  postInvolvementForm(form: InvolvementForm) {
    return this.http.post<any>(this.involvementFormUrl, this.toFormData(form));
  }

  private toFormData(form: any) {
    const data = new FormData();
    for (const key of Object.keys(form)) {
      data.append(key, form[key]);
    }
    return data;
  }
}

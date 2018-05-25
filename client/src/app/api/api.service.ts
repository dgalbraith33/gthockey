import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { Observable, ReplaySubject } from 'rxjs';
import { map } from 'rxjs/operators';

import { environment } from './../../environments/environment';
import { Article } from './article';
import { Board } from './board';
import { Coach } from './coach';
import { ContactForm } from './contact';
import { Game, GameMin } from './game';
import { InvolvementForm } from './involvement';
import { Order } from './order';
import { Player } from './player';
import { ProspectForm } from './prospect';
import { ShopItem } from './shop-item';

@Injectable()
export class ApiService {

  private readonly apiEndpoint: string;
  private readonly formEndpoint: string;

  private readonly rosterUrl: string;
  private readonly articleUrl: string;
  private readonly gameUrl: string;
  private readonly boardUrl: string;
  private readonly coachUrl: string;
  private readonly shopUrl: string;

  private readonly contactFormUrl: string;
  private readonly prospectFormUrl: string;
  private readonly involvementFormUrl: string;
  private readonly orderFormUrl: string;

  private cache: any = {};

  constructor(private http: HttpClient) {
    this.apiEndpoint = environment.apiurl + '/api/';
    this.formEndpoint = this.apiEndpoint + 'forms/';

    this.rosterUrl = this.apiEndpoint + 'players/';
    this.articleUrl = this.apiEndpoint + 'articles/';
    this.gameUrl = this.apiEndpoint +  'games/';
    this.boardUrl = this.apiEndpoint + 'board/';
    this.coachUrl = this.apiEndpoint + 'coaches/';
    this.shopUrl = this.apiEndpoint + 'shop/';

    this.contactFormUrl = this.formEndpoint + 'contact/';
    this.prospectFormUrl = this.formEndpoint + 'prospect/';
    this.involvementFormUrl = this.formEndpoint + 'involvement/';
    this.orderFormUrl = this.formEndpoint + 'order/';
   }

  getPlayers(): Observable<Player[]> {
    return this.getFromCache(this.rosterUrl);
  }

  getArticles(): Observable<Article[]> {
    return this.getFromCache(this.articleUrl);
  }

  getArticle(id: number): Observable<Article> {
    return this.getFromCache(this.articleUrl + id + '/');
  }

  getGames(params: any = {}): Observable<GameMin[]> {
    return this.http.get<GameMin[]>(this.gameUrl, {params}).pipe(map((games: GameMin[]) => games.map(game => new GameMin(game))));
  }

  getGame(id: number): Observable<Game> {
    return this.getFromCache(this.gameUrl + id + '/');
  }

  getBoard(): Observable<Board[]> {
    return this.getFromCache(this.boardUrl);
  }

  getCoaches(): Observable<Coach[]> {
    return this.getFromCache(this.coachUrl);
  }

  getShopItems(): Observable<ShopItem[]> {
    return this.getFromCache(this.shopUrl);
  }

  getShopItem(id: number): Observable<ShopItem> {
    return this.getFromCache(this.shopUrl + id + '/');
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

  postOrderForm(form: Order) {
    return this.http.post<any>(this.orderFormUrl, form, this.jsonHeaders());
  }

  private toFormData(form: any) {
    const data = new FormData();
    for (const key of Object.keys(form)) {
      data.append(key, form[key]);
    }
    return data;
  }

  private jsonHeaders(): any {
    return {headers: new HttpHeaders({'Content-type': 'application/json'})};
  }

  private getFromCache(url: string): Observable<any> {
    if (!this.cache[url]) {
      this.cache[url] = new ReplaySubject(1);
    }
    this.http.get(url).subscribe(result => this.cache[url].next(result));
    return this.cache[url];
  }
}

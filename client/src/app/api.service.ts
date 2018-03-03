import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable'

import { Player } from './api/player'

@Injectable()
export class ApiService {

  private rosterUrl = '/api/players'

  constructor(private http: HttpClient) { }

  getPlayers(): Observable<Player[]> {
    return this.http.get<Player[]>(this.rosterUrl);
  }

}

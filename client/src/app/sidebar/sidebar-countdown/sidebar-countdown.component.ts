import { Component, OnInit } from '@angular/core';

import {timer as observableTimer,  Observable } from 'rxjs';

import { ApiService } from '../../api/api.service';
import { GameMin } from '../../api/game';

@Component({
  selector: 'app-sidebar-countdown',
  templateUrl: './sidebar-countdown.component.html',
  styleUrls: ['./sidebar-countdown.component.css']
})
export class SidebarCountdownComponent implements OnInit {

  game: GameMin;
  image: string;

  readonly params = {
    date_from: SidebarCountdownComponent.getToday(),
    limit: 1,
  };

  private static getToday(): string {
    const date = new Date();
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
  }

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getUpcoming();
  }

  private getUpcoming() {
    this.apiService.getGames(this.params).subscribe(games => {
      if (games.length > 0) {
        this.game = games[0];
        this.apiService.getGame(this.game.id).subscribe(game => this.image = game.opponent.logo);
      }
    });
  }
}

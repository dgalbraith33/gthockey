import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/timer';
import { Component, OnInit } from '@angular/core';

import { ApiService } from '../../api.service';
import { GameMin } from '../../api/game';

@Component({
  selector: 'app-sidebar-countdown',
  templateUrl: './sidebar-countdown.component.html',
  styleUrls: ['./sidebar-countdown.component.css']
})
export class SidebarCountdownComponent implements OnInit {

  game: GameMin;
  image: string;

  diffSeconds: string;
  diffMinutes: string;
  diffHours: string;
  diffDays: string;

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
        this.startTimer();
        this.apiService.getGame(this.game.id).subscribe(game => this.image = game.opponent.logo);
      }
    });
  }


  private startTimer() {
    const timer = Observable.timer(0, 1000);
    timer.subscribe(t => this.updateTime());
  }

  private updateTime() {
    const diffMillis = this.game.date.getTime() - Date.now();

    this.diffSeconds = ((diffMillis / 1000) % 60).toFixed();
    this.diffMinutes = ((diffMillis / (60 * 1000)) % 60).toFixed();
    this.diffHours = ((diffMillis / (60 * 60 * 1000)) % 24).toFixed();
    this.diffDays = (diffMillis / (24 * 60 * 60 * 1000)).toFixed();
  }


}

import { Component, OnInit } from '@angular/core';

import { ApiService } from './../api.service';
import { Game } from '../api/game';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css']
})
export class ScheduleComponent implements OnInit {

  private games: Game[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getGames();
  }

  private getGames() {
    this.apiService.getGames().subscribe(games => this.games = games);
  }

}

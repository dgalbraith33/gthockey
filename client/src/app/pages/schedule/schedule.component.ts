import { Component, OnInit } from '@angular/core';

import { ApiService } from '../../api/api.service';
import { GameMin } from '../../api/game';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css']
})
export class ScheduleComponent implements OnInit {

  completedGames: GameMin[];
  upcomingGames: GameMin[];

  hasCompletedGames = false;
  hasUpcomingGames = false;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getGames();
  }

  private getGames() {
    this.apiService.getGames().subscribe(games => {
      this.completedGames = games.filter(game => game.is_reported);
      this.hasCompletedGames = this.completedGames.length > 0;
      this.upcomingGames = games.filter(game => !game.is_reported);
      this.hasUpcomingGames = this.upcomingGames.length > 0;
    });
  }

}

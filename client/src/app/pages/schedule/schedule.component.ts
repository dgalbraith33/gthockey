import { Component, OnInit } from '@angular/core';

import { ApiService } from '../../api/api.service';
import { GameMin } from '../../api/game';
import { Season } from '../../api/season';

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

  seasons: Season[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getSeasons();
    this.getGames();
  }

  private getSeasons() {
    this.apiService.getSeasons().subscribe(seasons => this.seasons = seasons.reverse());
  }

  private onChange(param: any) {
    console.log(param);
  }

  private getGames(season?: number) {
    const params = season ? {season} : {};
    this.hasCompletedGames = false;
    this.hasUpcomingGames = false;
    this.apiService.getGames(params).subscribe(games => {
      this.completedGames = games.filter(game => game.is_reported);
      this.hasCompletedGames = this.completedGames.length > 0;
      this.upcomingGames = games.filter(game => !game.is_reported);
      this.hasUpcomingGames = this.upcomingGames.length > 0;
    });
  }

}

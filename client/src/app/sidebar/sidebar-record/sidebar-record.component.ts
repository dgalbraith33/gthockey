import { Component, OnInit } from '@angular/core';

import { ApiService } from '../../api/api.service';
import { GameMin } from '../../api/game';

@Component({
  selector: 'app-sidebar-record',
  templateUrl: './sidebar-record.component.html',
  styleUrls: ['./sidebar-record.component.css']
})
export class SidebarRecordComponent implements OnInit {

  private wins: number;
  private losses: number;
  private otls: number;
  private ties: number;

  record: string;
  season: string;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getGames();
  }

  private getGames() {
    this.apiService.getGames().subscribe(games => {
        this.setRecord(games);
        this.composeRecord();
    });
    this.apiService.getCurrentSeason().subscribe(resp => this.season = resp.name);
  }

  private setRecord(games: GameMin[]) {
    this.wins = 0;
    this.losses = 0;
    this.otls = 0;
    this.ties = 0;
    games.forEach(game => {
        switch (game.short_result) {
            case('W'):
                this.wins++;
                break;
            case('L'):
                this.losses++;
                break;
            case('T'):
                this.ties++;
                break;
            case('OTL'):
                this.otls++;
                break;
        }
    });
    this.composeRecord();
  }

  private composeRecord() {
    this.record = [this.wins, this.losses, this.otls, this.ties].join('-');
  }
}

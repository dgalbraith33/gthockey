import { Component, OnInit } from '@angular/core';

import { ApiService } from './../api.service';
import { Game } from '../api/game';

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

  private record: string;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getGames();
  }

  private getGames() {
    this.apiService.getGames().subscribe(games => {
        this.setRecord(games);
        this.composeRecord();
    });
  }

  private setRecord(games: Game[]) {
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
    console.log(this);
    this.composeRecord();
  }

  private composeRecord() {
    this.record = [this.wins, this.losses, this.otls, this.ties].join('-');
  }
}

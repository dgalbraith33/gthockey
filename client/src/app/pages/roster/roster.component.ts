import { Component, OnInit } from '@angular/core';

import { ApiService } from '../../api/api.service';
import { Player } from '../../api/player';

@Component({
  selector: 'app-roster',
  templateUrl: './roster.component.html',
  styleUrls: ['./roster.component.css']
})
export class RosterComponent implements OnInit {

  players: Player[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getPlayers();
  }

  getPlayers() {
    this.apiService.getPlayers().subscribe(players => this.players = players);
  }

}

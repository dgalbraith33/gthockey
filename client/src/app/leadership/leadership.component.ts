import { Component, OnInit } from '@angular/core';

import { ApiService } from './../api.service';
import { Board } from '../api/board';
import { Coach } from '../api/coach';


@Component({
  selector: 'app-leadership',
  templateUrl: './leadership.component.html',
  styleUrls: ['./leadership.component.css']
})
export class LeadershipComponent implements OnInit {

  board: Board[];
  coaches: Coach[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getBoard();
    this.getCoaches();
  }

  private getBoard() {
    this.apiService.getBoard().subscribe(board => this.board = board);
  }

  private getCoaches() {
    this.apiService.getCoaches().subscribe(coaches => this.coaches = coaches);
  }

}

import { Component, OnInit } from '@angular/core';

import { ApiService } from './../../api/api.service';
import { Article } from '../../api/article';

@Component({
  selector: 'app-frontpage',
  templateUrl: './frontpage.component.html',
  styleUrls: ['./frontpage.component.css']
})
export class FrontpageComponent implements OnInit {

  articles: Article[];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getArticles();
  }

  private getArticles() {
    this.apiService.getArticles().subscribe(articles => this.articles = articles);
  }

}

import { Component, OnInit } from '@angular/core';

import { ApiService } from './../../api/api.service';
import { Article } from '../../api/article';

@Component({
  selector: 'app-frontpage',
  templateUrl: './frontpage.component.html',
  styleUrls: ['./frontpage.component.css']
})
export class FrontpageComponent implements OnInit {

  leadArticle: Article;
  currentArticles: Article[];
  currentPage: number;
  startIndex: number;
  pageNumbers: number[];
  articles: Article[];

  private readonly perPage = 5;
  private numPages: number;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getArticles();
  }

  private getArticles() {
    this.apiService.getArticles().subscribe(articles => {
      this.articles = articles.slice(1);
      this.leadArticle = articles[0];
      this.numPages = Math.ceil(this.articles.length / 5);
      this.pageNumbers = Array(this.numPages).fill(0).map((x, i) => i + 1);
      this.updatePage(1);
    });
  }

  updatePage(page: number) {
    if (page <= 0 || page > this.numPages) {
      return;
    }
    this.currentPage = page;
    page--;
    this.startIndex = page * this.perPage;
    this.currentArticles = this.articles.slice(this.startIndex, this.startIndex + this.perPage);
  }

}

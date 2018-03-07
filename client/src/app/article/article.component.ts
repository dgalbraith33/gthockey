import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Article } from '../api/article';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-article',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {

  private id: number;
  private article: Article;
  private loaded = false;

  constructor(private route: ActivatedRoute,
              private apiService: ApiService) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get('id'), 10);
    this.getArticle();
  }

  private getArticle() {
    this.apiService.getArticle(this.id).subscribe(article => this.article = article);
  }
}

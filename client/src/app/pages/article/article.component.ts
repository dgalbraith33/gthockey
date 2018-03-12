import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { ApiService } from '../../api/api.service';
import { Article } from '../../api/article';

@Component({
  selector: 'app-article',
  templateUrl: './article.component.html',
  styleUrls: ['./article.component.css']
})
export class ArticleComponent implements OnInit {

  private id: number;
  article: Article;
  paragraphs: string[];

  constructor(private route: ActivatedRoute,
              private apiService: ApiService) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get('id'), 10);
    this.getArticle();
  }

  private getArticle() {
    this.apiService.getArticle(this.id).subscribe(article => {
      this.article = article;
      this.paragraphs = article.content.split('\n');
    });
  }
}

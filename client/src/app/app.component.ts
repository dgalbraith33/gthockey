import { Component } from '@angular/core';

import { Angulartics2GoogleAnalytics } from 'angulartics2/ga';

import { environment } from './../environments/environment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(angularitcs2GoogleAnalytics: Angulartics2GoogleAnalytics) {}
}

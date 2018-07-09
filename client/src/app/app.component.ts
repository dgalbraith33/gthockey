import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';

import { Angulartics2GoogleAnalytics } from 'angulartics2/ga';

import { environment } from './../environments/environment';
import { CartService } from './cart/cart.service';

declare var UIkit: any;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  constructor(
    angularitcs2GoogleAnalytics: Angulartics2GoogleAnalytics,
    readonly cartService: CartService,
    private router: Router) {
    }

  ngOnInit() {
    const dropdown = UIkit.dropdown('.uk-navbar-dropdown', {offset: 0});
    this.router.events.subscribe( (event) => {
      if (event instanceof NavigationEnd) {
        dropdown.hide(false);
      }
    });

  }
}

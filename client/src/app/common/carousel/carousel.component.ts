import { Component, OnInit, Input } from '@angular/core';

import { CarouselItem } from './carousel';

@Component({
  selector: 'app-carousel',
  templateUrl: './carousel.component.html',
  styleUrls: ['./carousel.component.css']
})
export class CarouselComponent implements OnInit {

  @Input()
  carouselItems: CarouselItem[];

  constructor() { }

  ngOnInit() {
  }

}

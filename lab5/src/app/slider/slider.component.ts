import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-slider',
  templateUrl: './slider.component.html',
  styleUrls: ['./slider.component.scss']
})
export class SliderComponent implements OnInit {

  slides: any[] = new Array(3).fill({id: -1, src: '', title: '', subtitle: ''});

  constructor() { }

  ngOnInit(): void {
    this.slides[0] = {
      src: 'https://m.media-amazon.com/images/I/71xb2xkN5qL._AC_UF894,1000_QL80_.jpg',
    };
    this.slides[1] = {
      src: 'https://activ.kz/shop/media/__sized__/products/iphone_13_pro123456_oXbD4y9-thumbnail-255x255-90.jpg',
    }
    this.slides[2] = {
      src: 'https://media.wired.com/photos/6148ef98a680b1f2086efee0/1:1/w_1037,h_1037,c_limit/Gear-Review-Apple_iphone13_hero_us_09142021.jpg',
    }
  }
}
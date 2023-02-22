import { Component } from '@angular/core';
import { CartService } from '../cart.service';
import {  products } from '../products';
@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent {
  products= products;
  items = this.cartService.getItems();
  constructor(
    private cartService: CartService,
  ){}
}

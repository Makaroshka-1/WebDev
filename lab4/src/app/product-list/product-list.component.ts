import { Component } from '@angular/core';
import { Product, products } from '../products';
import { CartService }from '../cart.service';
@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss']
})
export class ProductListComponent {
  products = products;
  constructor(
    private cartService : CartService,
  ){}
  
  share(){
    alert("are you sure?");
  };
  addToCart(product: Product){
    this.cartService.addToCart(product);
    window.alert('Your product has been added to the cart!');
  }
}

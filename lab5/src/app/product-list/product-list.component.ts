import { Component } from '@angular/core';
import { Product, products } from '../products';
import { CartService }from '../cart.service';
import { LikeServiceService } from '../like-service.service';
@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss']
})
export class ProductListComponent {
  products = products;
  constructor(
    private cartService : CartService,
    private likeServiceService:LikeServiceService,
  ){}
  
  share(){
    alert("are you sure?");
  };
  addToCart(product: Product){
    this.cartService.addToCart(product);
    window.alert('Your product has been added to the cart!');
  }
  addToLiked(product: Product){
    this.likeServiceService.addToLiked(product);
    window.alert('Added to liked');
  }
}

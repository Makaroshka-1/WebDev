import { Injectable } from '@angular/core';
import { Product } from './products'  
@Injectable({
  providedIn: 'root'
})
export class CartService {
  items: Product[] = [];
  constructor() { }

  addToCart (product: Product){
    this.items.push(product);
  }
  clearcart(){
    this.items = [];
    return this.items;
  }
  getItems(){
    return this.items;
  }
}

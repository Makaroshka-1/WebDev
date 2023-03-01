import { Injectable } from '@angular/core';
import { Product } from './products';

@Injectable({
  providedIn: 'root'
})
export class LikeServiceService {
  items : Product[] = [];
  constructor() { }

  addToLiked (product: Product){
    this.items.push(product);
  }
  clearLiked(){
    this.items = [];
    return this.items;
  }
  getItems(){
    return this.items;
  }
}

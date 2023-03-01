import { Component } from '@angular/core';
import {products } from "../products"
import { LikeServiceService } from '../like-service.service';
@Component({
  selector: 'app-likes',
  templateUrl: './likes.component.html',
  styleUrls: ['./likes.component.scss']
})
export class LikesComponent {
  products= products;
  items = this.likeServiceService.getItems();
  constructor(
    private likeServiceService:LikeServiceService,
  ){}
}

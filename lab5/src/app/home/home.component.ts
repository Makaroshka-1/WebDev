import { Component, OnInit } from '@angular/core';
import { Product,products } from '../products';
import { CartService } from '../cart.service';
import { ActivatedRoute } from '@angular/router';
import { LikeServiceService } from '../like-service.service';
import { ProductListComponent } from '../product-list/product-list.component';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit{
  product : Product |undefined;
  products=products;

  constructor(
    private route: ActivatedRoute,
    private cartService: CartService,
  ) {}
  ngOnInit(){
    const routeParams = this.route.snapshot.paramMap;
    const productCategorieFromRoute = String(routeParams.get('productCategorie'));
}
}

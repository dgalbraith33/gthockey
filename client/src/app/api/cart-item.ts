import { ShopItem } from './shop-item';

export class CartItem {

    item_id: number;
    options: any = {};
    custom_options: any = {};

    constructor(readonly shopItem: ShopItem) {
        this.item_id = this.shopItem.id;
    }
}

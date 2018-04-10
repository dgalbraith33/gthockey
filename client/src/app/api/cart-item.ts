import { ShopItem } from './shop-item';

export class CartItem {

    item_id: number;
    options: any = {};
    custom_options: any = {};

    constructor(readonly shopItem: ShopItem) {
        this.item_id = this.shopItem.id;
    }

    getOptions(): any[] {
        const option_list = [];
        for (const option_id of Object.keys(this.options)) {
            for (const option of this.shopItem.options) {
                if (option.id === Number.parseInt(option_id)) {
                    option_list.push(option.display_name + ':' + this.options[option_id]);
                }
            }
        }
        return option_list;
    }

    getCustomOptions(): any[] {
        const option_list = [];
        for (const option_id of Object.keys(this.custom_options)) {
            for (const option of this.shopItem.custom_options) {
                if (option.id === Number.parseInt(option_id)) {
                    option_list.push(option.display_name + ':' + this.custom_options[option_id]);
                }
            }
        }
        return option_list;
    }
}

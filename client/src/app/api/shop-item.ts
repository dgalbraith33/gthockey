export class ShopItemImage {
    image: string;
}

export class ShopItemOptionList {
    id: number;
    display_name: string;
    help_text: string;
    option_list: string;
}

export class ShopItemCustomOption {
    id: number;
    display_name: string;
    help_text: string;
    required: boolean;
    extra_cost: number;
}

export class ShopItem {
    id: number;
    name: string;
    price: number;
    description: string;
    in_stock: boolean;
    image: string;
    images: ShopItemImage[];
    options: ShopItemOptionList[];
    custom_options: ShopItemCustomOption[];
}

import { CartItem } from './cart-item';

export class Order {
    name: string;
    address: string;
    phone: string;
    email: string;
    items: CartItem[];
    message: string;
    captcha: string;
}

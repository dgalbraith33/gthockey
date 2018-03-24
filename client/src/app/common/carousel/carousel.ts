export class CarouselItem {
    image: string;
    text: string;
    route: string;

    constructor(image?: string, text?: string, route?: string) {
        this.image = image;
        this.text = text;
        this.route = route;
    }
}

export class InvolvementForm {
    name: string;
    email: string;
    relation: number;
    captcha: string;

    constructor() {
        this.relation = 0;
    }
}

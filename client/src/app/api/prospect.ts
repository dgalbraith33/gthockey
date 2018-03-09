export class ProspectForm {
    name: string;
    email: string;
    phone: string;
    birth: string;
    hometown: string;
    status: number;
    experience: string;
    position: number;
    comments: string;
    captcha: string;

    constructor() {
        this.status = 0;
        this.position = 0;
    }
}

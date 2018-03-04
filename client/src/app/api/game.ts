export class Opponent {
    school_name: string;
    mascot_name: string;

    public constructor(serverModel: any) {
        this.school_name = serverModel.school_name;
        this.mascot_name = serverModel.mascot_name;
    }
}

export class Game {
    id: number;
    date: Date;
    opponent: Opponent;
    venue: string;
    location: string;
    short_result: string;
    score_gt_final: number;
    score_opp_final: number;

    public constructor(serverModel: any) {
        this.id = serverModel.id;
        this.date = new Date(serverModel.date + ' ' + serverModel.time);
        this.opponent = new Opponent(serverModel.opponent);
        this.venue = serverModel.venue;
        this.location = serverModel.location.rink_name;
        this.short_result = serverModel.short_result;
        this.score_gt_final = serverModel.score_gt_final;
        this.score_opp_final = serverModel.score_opp_final;
    }

    public isOver(): boolean {
        return this.score_gt_final !== null && this.score_opp_final !== null;
    }
}

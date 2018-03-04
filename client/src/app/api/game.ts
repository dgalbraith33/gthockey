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
    is_reported: boolean;
    short_result: string;
    score_gt_final: number;
    score_opp_final: number;

    public constructor(serverModel: any) {
        this.id = serverModel.id;
        this.date = new Date(serverModel.datetime);
        this.opponent = serverModel.opponent_name;
        this.venue = serverModel.venue;
        this.location = serverModel.rink_name;
        this.is_reported = serverModel.is_reported;
        this.short_result = serverModel.short_result;
        this.score_gt_final = serverModel.gt_score;
        this.score_opp_final = serverModel.opp_score;
    }

    public isOver(): boolean {
        return this.score_gt_final !== null && this.score_opp_final !== null;
    }
}

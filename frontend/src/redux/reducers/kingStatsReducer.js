// Step 3: Create reducers for the action types
import {UPDATE_KING, UPDATE_KING_METADATA, UPDATE_KING_BATTLE_RATINGS_LINE_DATA,
        UPDATE_KING_BATTLE_WIN_LOSS_PIE_CHART_DATA, UPDATE_KING_BATTLE_DETAILS_TABLE_DATA,
        UPDATE_BATTLE_STATS_TABLE_DATA, UPDATE_BATTLE_STATS_COLUMN_CHART_DATA} from "../actionTypes";

const initialState = { 
    king : "",
    kingMetaData : {},
    kingBattleRatingsLineData : [],
    kingBattleWinLossPieChartData : [] ,
    kingBattleDetailsTableData : [],
    battleStatsTableData : [],
    battleStatsColumnChartData : [] 
};

const kingStatsReducer = (state=initialState, actions) => {
    switch(actions.type) {
        case UPDATE_KING:
            return {...state, king: actions.payload.king};
        case UPDATE_KING_METADATA:
            return {...state, kingMetaData: actions.payload.kingMetaData};
        case UPDATE_KING_BATTLE_RATINGS_LINE_DATA:
            return {...state, kingBattleRatingsLineData: actions.payload.kingBattleRatingsLineData};
        case UPDATE_KING_BATTLE_WIN_LOSS_PIE_CHART_DATA:
            return {...state, kingBattleWinLossPieChartData: actions.payload.kingBattleWinLossPieChartData};
        case UPDATE_KING_BATTLE_DETAILS_TABLE_DATA:
            return {...state, kingBattleDetailsTableData: actions.payload.kingBattleDetailsTableData};
        case UPDATE_BATTLE_STATS_TABLE_DATA:
            return {...state, battleStatsTableData: actions.payload.battleStatsTableData};
        case UPDATE_BATTLE_STATS_COLUMN_CHART_DATA:
            return {...state, battleStatsColumnChartData: actions.payload.battleStatsColumnChartData};
        default:
            return {...state};
    }
};

export default kingStatsReducer;
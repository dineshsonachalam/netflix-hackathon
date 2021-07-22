// Step 2: Create Actions for your Action Types

import {UPDATE_KING, UPDATE_KING_METADATA, UPDATE_KING_BATTLE_RATINGS_LINE_DATA, 
        UPDATE_KING_BATTLE_WIN_LOSS_PIE_CHART_DATA, UPDATE_KING_BATTLE_DETAILS_TABLE_DATA,
        UPDATE_BATTLE_STATS_TABLE_DATA, UPDATE_BATTLE_STATS_COLUMN_CHART_DATA} from "./actionTypes";

export const updateKing = (king) => {
    return {
              type: UPDATE_KING,
              payload: {
                king: king
              }
    }
}

export const updateKingMetaData = (kingMetaData) => {
  return {
            type: UPDATE_KING_METADATA,
            payload: {
              kingMetaData: kingMetaData
            }
  }
}

export const updateKingBattleRatingsLineData = (kingBattleRatingsLineData) => {
  return {
            type: UPDATE_KING_BATTLE_RATINGS_LINE_DATA,
            payload: {
              kingBattleRatingsLineData: kingBattleRatingsLineData
            }
  }
}

export const updateKingBattleWinLossPieChartData = (kingBattleWinLossPieChartData) => {
  return {
            type: UPDATE_KING_BATTLE_WIN_LOSS_PIE_CHART_DATA,
            payload: {
              kingBattleWinLossPieChartData: kingBattleWinLossPieChartData
            }
  }
}

export const updateKingBattleDetailsTableData = (kingBattleDetailsTableData) => {
  return {
            type: UPDATE_KING_BATTLE_DETAILS_TABLE_DATA,
            payload: {
              kingBattleDetailsTableData: kingBattleDetailsTableData
            }
  }
}

export const updateBattleStatsTableData = (battleStatsTableData) => {
  return {
            type: UPDATE_BATTLE_STATS_TABLE_DATA,
            payload: {
              battleStatsTableData: battleStatsTableData
            }
  }
}

export const updateBattleStatsColumnChartData = (battleStatsColumnChartData) => {
  return {
            type: UPDATE_BATTLE_STATS_COLUMN_CHART_DATA,
            payload: {
              battleStatsColumnChartData: battleStatsColumnChartData
            }
  }
}

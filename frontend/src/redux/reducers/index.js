// Step 3: Create reducers for the action types

import { combineReducers } from "redux";

import kingStatsReducer from "./kingStatsReducer";

export default combineReducers({ kingStatsReducer });
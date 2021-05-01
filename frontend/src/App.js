import React from 'react';
import KingBattleRatingsLine from './components/KingBattleRatingsLine';
import KingBattleWinLossPieChart from './components/KingBattleWinLossPieChart';
import KingBattleDetailsTable from './components/KingBattleDetailsTable';
import BattleStatsColumnChart from "./components/BattleStatsColumnChart";
import BattleStatsTable from './components/BattleStatsTable';
import KingDropDown from './components/KingDropDown';

import Nav from "./components/Nav"
import {  updateBattleStatsTableData, 
          updateBattleStatsColumnChartData, updateKingMetaData } from "./redux/actions";
import { connect } from 'react-redux';

import { Layout} from 'antd';

const { Footer, Content } = Layout;

class App extends React.Component {
  async getData(url) {
    const response = await fetch(url);
    return response.json();
  }

  async componentDidMount(){
      let url = "http://0.0.0.0:8082/battles"
      const results = await this.getData(url);
      this.props.updateBattleStatsTableData(results["info"]);
      this.props.updateBattleStatsColumnChartData(results["win_loss_data"]);
      this.props.updateKingMetaData(results["stats"]);
  }
  render(){
    return (
      <div className="App">
        <Nav />  
        <Content>
            <div style={{ padding: 24}}>
                    <KingDropDown/>
                    {this.props.king &&
                      <div>
                        <KingBattleRatingsLine/>
                        <KingBattleWinLossPieChart/>
                        <KingBattleDetailsTable/>
                        <BattleStatsColumnChart/>
                        <BattleStatsTable/>
                      </div>
                    }
            </div>
        </Content>
        <div  style={ (this.props.king) ? {}: { position:"absolute", bottom:0, color: "blue", width:"100%"  } }>
            <Footer style={{ textAlign: 'center' }}> Developed with ❤️ by <a href="https://github.com/dineshsonachalam/ADP-NY-HACKATHON" rel="noreferrer" target="_blank">Dinesh Sonachalam</a> © {(new Date().getFullYear())}</Footer> 
        </div>
      </div>
    );
  }
}


const mapStateToProps = (state) => {
  return state.kingStatsReducer;
}

const mapDispatchToProps = (dispatch) => {
  return {
    updateBattleStatsTableData: (battleStatsTableData) => dispatch(updateBattleStatsTableData(battleStatsTableData)),
    updateBattleStatsColumnChartData: (battleStatsColumnChartData) => dispatch(updateBattleStatsColumnChartData(battleStatsColumnChartData)),
    updateKingMetaData: (kingMetaData) => dispatch(updateKingMetaData(kingMetaData))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App);


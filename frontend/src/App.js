import React from 'react';
import SearchBar from './components/SearchBar';
import SearchResults from "./components/SearchResults";
import BattleStatsColumnChart from "./components/BattleStatsColumnChart";
import KingBattleWinLossPieChart from './components/KingBattleWinLossPieChart';
import KingBattleRatingsLine from './components/KingBattleRatingsLine';
import BattleStatsTable from './components/BattleStatsTable';
import KingBattleDetailsTable from './components/KingBattleDetailsTable';
import KingDropDown from './components/KingDropDown';

import Nav from "./components/Nav"
import { connect } from 'react-redux';

import { Layout} from 'antd';
const { Footer, Content } = Layout;

class App extends React.Component {
  render(){
    return (
      <div className="App">
        <Nav />  
        <Content>
            <div style={{ padding: 24}}>
                    {/* <center>
                      <SearchBar />
                    </center>
                    <div style={{ padding: 24}}>
                      <SearchResults />
                    </div> */}
                    <BattleStatsColumnChart/>
                    <KingBattleWinLossPieChart/>
                    <KingBattleRatingsLine/>
                    <BattleStatsTable/>
                    <KingBattleDetailsTable/>
                    <KingDropDown/>
            </div>
        </Content>
        {/* <div  style={ (this.props.search_results).length>0 ? {}: { position:"absolute", bottom:0, color: "blue", width:"100%"  } }>
            <Footer style={{ textAlign: 'center' }}> Developed with ❤️ by <a href="https://github.com/dineshsonachalam/ADP-NY-HACKATHON" rel="noreferrer" target="_blank">Dinesh Sonachalam</a> © {(new Date().getFullYear())}</Footer> 
        </div> */}
      </div>
    );
  }

}


const mapStateToProps = (state) => {
  return state.searchReducer;
}

const mapDispatchToProps = (dispatch) => {
  return {}
}

export default connect(mapStateToProps, mapDispatchToProps)(App);


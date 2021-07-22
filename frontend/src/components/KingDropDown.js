import React from "react";
import { Select, Image } from "antd";
import { updateKing, updateKingBattleRatingsLineData, 
         updateKingBattleWinLossPieChartData, updateKingBattleDetailsTableData } from "../redux/actions";
import { connect } from "react-redux";


const { Option } = Select;

class KingDropDown extends React.Component {
    constructor(props) {
        super(props);
        this.state = {"kingImageURL": ""};
    }
    onChange = (value) => {
        this.props.updateKing(value);
        let kingBattleData = value;
        this.props.updateKingBattleRatingsLineData(kingBattleData["rating_info"]);
        this.props.updateKingBattleWinLossPieChartData(kingBattleData["win_loss_stats"]);
        this.props.updateKingBattleDetailsTableData(kingBattleData["battle_details"]);
        if(value === "Joffrey/Tommen Baratheon"){
            this.setState({
                "kingImageURL": "https://cdn.shopify.com/s/files/1/0528/2139/3573/products/King.jpg"
            });
        }else if(value === "Robb Stark"){
            this.setState({
                "kingImageURL": "https://static.wikia.nocookie.net/goff/images/5/50/S3E9_Robb_Stark_main.jpg"
            });
        }else if(value === "Balon/Euron Greyjoy"){
            this.setState({
                "kingImageURL": "https://static.wikia.nocookie.net/gameofthrones/images/f/fc/Euron-Profile.PNG"
            });
        }else if(value === "Stannis Baratheon"){
            this.setState({
                "kingImageURL": "https://static.wikia.nocookie.net/gameofthrones/images/2/2f/StannisNew.png"
            });
        }else if(value === "Renly Baratheon"){
            this.setState({
                "kingImageURL": "https://static.wikia.nocookie.net/gameofthrones/images/f/ff/Profile-Renly_Baratheon.png"
            });
        }
    }

    onBlur() {}
    onFocus() {}
    onSearch(val) {}

    render() {
            return (
                <div style={{ padding: 0}}>
                    <center>
                        <Select
                        showSearch
                        style={{ width: 200 }}
                        placeholder="Select a king"
                        optionFilterProp="children"
                        onChange={this.onChange}
                        onFocus={this.onFocus}
                        onBlur={this.onBlur}
                        onSearch={this.onSearch}
                        filterOption={(input, option) =>
                        option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
                        }
                        >
                            <Option value="Joffrey/Tommen Baratheon">Joffrey/Tommen Baratheon</Option>
                            <Option value="Robb Stark">Robb Stark</Option>
                            <Option value="Balon/Euron Greyjoy">Balon/Euron Greyjoy</Option>
                            <Option value="Stannis Baratheon">Stannis Baratheon</Option>
                            <Option value="Renly Baratheon">Renly Baratheon</Option>
                        </Select>
                    </center>
                    {this.props.king && this.state.kingImageURL &&
                        
                        <center>    
                            <div style={{ padding: 20}}>
                            <Image
                            width={220}
                            src={this.state.kingImageURL}
                            />
                            </div>
                        </center>
                    }    
                </div>
            );
    }
}

// https://stackoverflow.com/a/50225424
const mapStateToProps = (state) => {
    return state.kingStatsReducer;
};
  
const mapDispatchToProps = (dispatch) => {
    return {
      updateKing: (king) => dispatch(updateKing(king)),
      updateKingBattleRatingsLineData: (kingBattleRatingsLineData) => dispatch(updateKingBattleRatingsLineData(kingBattleRatingsLineData)),
      updateKingBattleWinLossPieChartData: (kingBattleWinLossPieChartData) => dispatch(updateKingBattleWinLossPieChartData(kingBattleWinLossPieChartData)),
      updateKingBattleDetailsTableData: (kingBattleDetailsTableData) => dispatch(updateKingBattleDetailsTableData(kingBattleDetailsTableData))
    };
};
  
export default connect(mapStateToProps, mapDispatchToProps)(KingDropDown);




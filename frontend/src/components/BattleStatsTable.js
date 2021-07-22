import React from "react";
import { Table, PageHeader} from "antd";
import { connect } from "react-redux";
class BattleStatsTable extends React.Component { 
      render() {
            const columns = [
                  {
                        title: "Rank",
                        dataIndex: "rank",
                        key: "rank",
                  },
                  {
                        title: "King",
                        dataIndex: "king",
                        key: "king"
                  },
                  {
                        title: "Rating",
                        dataIndex: "rating",
                        key: "rating",
                  },
                  {
                        title: "Wins",
                        dataIndex: "wins",
                        key: "wins",
                  },
                  {
                        title: "Loss",
                        dataIndex: "loss",
                        key: "loss",
                  },
                  {
                        title: "Battles",
                        dataIndex: "battles",
                        key: "battles",
                  }
            ];        
            return (
                <div>
                        {(this.props.battleStatsTableData).length>0 &&     
                              <div className="site-page-header-ghost-wrapper">
                              <PageHeader
                                title="Kings ranking"
                              >
                                    <Table columns={columns} dataSource={this.props.battleStatsTableData} />
                              </PageHeader>
                              </div> 
                        }
                </div>
            );
      }
}



const mapStateToProps = (state) => {
      return state.kingStatsReducer;
};
    
const mapDispatchToProps = (dispatch) => {
      return {};
};
    
export default connect(mapStateToProps, mapDispatchToProps)(BattleStatsTable);
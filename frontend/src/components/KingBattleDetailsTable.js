import React from "react";
import { Table, PageHeader } from "antd";
import { connect } from "react-redux";

class KingBattleDetailsTable extends React.Component {
      render() {
            const columns = [
                  {
                        title: "Year",
                        dataIndex: "year",
                        key: "year"
                  },
                  {
                        title: "Role",
                        dataIndex: "role",
                        key: "role",
                  },
                  {
                        title: "Opponent",
                        dataIndex: "opponent",
                        key: "opponent",
                  },
                  {
                        title: "Battle Outcome",
                        dataIndex: "battle_outcome",
                        key: "battle_outcome",
                  },
                  {
                        title: "Rating",
                        dataIndex: "rating",
                        key: "rating",
                  }
            ];
            return (
                <div>
                        {this.props.king &&
                            
                            <div className="site-page-header-ghost-wrapper">
                            <PageHeader
                              title="Battle details"
                            >
                                <Table columns={columns} dataSource={this.props.kingMetaData[this.props.king]["battle_details"]} />
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
  
export default connect(mapStateToProps, mapDispatchToProps)(KingBattleDetailsTable);



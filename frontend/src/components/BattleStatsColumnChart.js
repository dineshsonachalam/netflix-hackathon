import React from "react";
import { Column } from "@ant-design/charts";
import { connect } from "react-redux";
import { PageHeader} from "antd";

class BattleStatsColumnChart extends React.Component {

      render() {
            const config = {
                  data: this.props.battleStatsColumnChartData,
                  isGroup: true,
                  xField: "king",
                  yField: "value",
                  seriesField: "name",
                  label: {
                    position: "middle",
                    layout: [
                      { type: "interval-adjust-position" },
                      { type: "interval-hide-overlap" },
                      { type: "adjust-color" },
                    ]
                  },
            };
            return (
                <div>
                      {(this.props.battleStatsColumnChartData).length>0 &&
                        <div className="site-page-header-ghost-wrapper">
                        <PageHeader
                          title="Battle statistics"
                        >
                            <Column {...config} />
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
    
export default connect(mapStateToProps, mapDispatchToProps)(BattleStatsColumnChart);


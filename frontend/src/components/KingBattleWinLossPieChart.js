import React from 'react';
import { Pie } from '@ant-design/charts';
import { connect } from 'react-redux';
import { PageHeader} from 'antd';
class KingBattleWinLossPieChart extends React.Component {
      render() {
        let data = [];
        if(this.props.king){
          data = this.props.kingMetaData[this.props.king]["win_loss_stats"];
        }
        var config = {
            appendPadding: 10,
            data: data,
            angleField: 'value',
            colorField: 'type',
            radius: 0.9,
            label: {
              type: 'inner',
              offset: '-30%',
              content: function content(_ref) {
                var percent = _ref.percent;
                return ''.concat(percent * 100, '%');
              },
              style: {
                fontSize: 14,
                textAlign: 'center',
              },
            },
            interactions: [{ type: 'element-active' }],
        };
            return (
                <div>
                    {this.props.king &&
                      <div className="site-page-header-ghost-wrapper">
                      <PageHeader
                        title="Battle win vs loss percentage"
                      >
                          <Pie {...config} />
                      </PageHeader>
                      </div> 
                    }
                </div>
            );
      }
}


const mapStateToProps = (state) => {
  return state.kingStatsReducer;
}

const mapDispatchToProps = (dispatch) => {
  return {}
}

export default connect(mapStateToProps, mapDispatchToProps)(KingBattleWinLossPieChart);



import React from 'react';
import { Line } from '@ant-design/charts';
import { connect } from 'react-redux';
import { PageHeader } from 'antd';
class KingBattleRatingsLine extends React.Component {
      render() {
            let data = [];
            if(this.props.king){
              data = this.props.kingMetaData[this.props.king]["rating_info"];
            }
            var config = {
                  data: data,
                  xField: 'battle',
                  yField: 'rating',
                  label: {},
                  point: {
                    size: 5,
                    shape: 'circle',
                    style: {
                      fill: 'white',
                      stroke: '#5B8FF9',
                      lineWidth: 2,
                    },
                  },
                  tooltip: { showMarkers: false },
                  state: {
                    active: {
                      style: {
                        shadowColor: 'yellow',
                        shadowBlur: 4,
                        stroke: 'transparent',
                        fill: 'red',
                      },
                    },
                  },
                  theme: {
                    geometries: {
                      point: {
                        diamond: {
                          active: {
                            style: {
                              shadowColor: '#FCEBB9',
                              shadowBlur: 2,
                              stroke: '#F6BD16',
                            },
                          },
                        },
                      },
                    },
                  },
                  interactions: [{ type: 'marker-active' }],
            };
            return (
                <div>
                      {this.props.king &&
                          <div className="site-page-header-ghost-wrapper">
                          <PageHeader
                            title="Ratings for each battle"
                          >
                              <Line {...config} />
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

export default connect(mapStateToProps, mapDispatchToProps)(KingBattleRatingsLine);





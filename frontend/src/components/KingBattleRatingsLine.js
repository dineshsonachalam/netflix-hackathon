import React from 'react';
import { Line } from '@ant-design/charts';

class KingBattleRatingsLine extends React.Component {
      render() {
            var data = [
                  {
                        battle: '1',
                        rating: 988.8363438391959,
                  },
                  {
                        battle: '2',
                        rating: 1088.8363438391959,
                  },
                  {
                        battle: '3',
                        rating: 992.8363438391959,
                  },
                  {
                        battle: '4',
                        rating: 992.8363438391959,
                  },
                  {
                        battle: '5',
                        rating: 988.8363438391959,
                  },
                  {
                        battle: '6',
                        rating: 1088.8363438391959,
                  },
                  {
                        battle: '7',
                        rating: 992.8363438391959,
                  }
            ];
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
                      <Line {...config} />
                </div>
            );
      }
}

export default KingBattleRatingsLine;



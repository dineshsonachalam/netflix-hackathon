import React from 'react';
import { Column } from '@ant-design/charts';

class BattleStatsColumnChart extends React.Component {

      render() {
            let data = [
                  {'name': 'Total Battles', 'king': 'Joffrey/Tommen Baratheon', 'value': 15
                  },
                  {'name': 'Total Wins', 'king': 'Joffrey/Tommen Baratheon', 'value': 8
                  },
                  {'name': 'Total Loss', 'king': 'Joffrey/Tommen Baratheon', 'value': 7
                  },
                  {'name': 'Total Battles', 'king': 'Robb Stark', 'value': 19
                  },
                  {'name': 'Total Wins', 'king': 'Robb Stark', 'value': 8
                  },
                  {'name': 'Total Loss', 'king': 'Robb Stark', 'value': 11
                  },
                  {'name': 'Total Battles', 'king': 'Balon/Euron Greyjoy', 'value': 7
                  },
                  {'name': 'Total Wins', 'king': 'Balon/Euron Greyjoy', 'value': 5
                  },
                  {'name': 'Total Loss', 'king': 'Balon/Euron Greyjoy', 'value': 2
                  },
                  {'name': 'Total Battles', 'king': 'Stannis Baratheon', 'value': 2
                  },
                  {'name': 'Total Wins', 'king': 'Stannis Baratheon', 'value': 1
                  },
                  {'name': 'Total Loss', 'king': 'Stannis Baratheon', 'value': 1
                  },
                  {'name': 'Total Battles', 'king': 'Renly Baratheon', 'value': 1
                  },
                  {'name': 'Total Wins', 'king': 'Renly Baratheon', 'value': 0
                  },
                  {'name': 'Total Loss', 'king': 'Renly Baratheon', 'value': 1
                  }
              ];
            let config = {
                  data: data,
                  isGroup: true,
                  xField: 'king',
                  yField: 'value',
                  seriesField: 'name',
                  label: {
                    position: 'middle',
                    layout: [
                      { type: 'interval-adjust-position' },
                      { type: 'interval-hide-overlap' },
                      { type: 'adjust-color' },
                    ]
                  },
            };
            return (
                <div>
                       <Column {...config} />
                </div>
            );
      }
}

export default BattleStatsColumnChart



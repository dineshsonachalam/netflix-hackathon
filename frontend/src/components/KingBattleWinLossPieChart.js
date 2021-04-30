import React from 'react';
import { Pie } from '@ant-design/charts';

class KingBattleWinLossPieChart extends React.Component {
      render() {
        var data = [
          {
              "type": "Win",
              "value": 53
          },
          {
              "type": "Loss",
              "value": 47
          }
      ];
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
                    <Pie {...config} />
                </div>
            );
      }
}

export default KingBattleWinLossPieChart



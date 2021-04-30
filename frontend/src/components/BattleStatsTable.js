import React from 'react';
import { Table, Tag, Space } from 'antd';

class BattleStatsTable extends React.Component {
      render() {
            const columns = [
                  {
                        title: 'King',
                        dataIndex: 'king',
                        key: 'king',
                        render: text => <a>{text}</a>,
                  },
                  {
                        title: 'Rating',
                        dataIndex: 'rating',
                        key: 'rating',
                  },
                  {
                        title: 'Wins',
                        dataIndex: 'wins',
                        key: 'wins',
                  },
                  {
                        title: 'Loss',
                        dataIndex: 'loss',
                        key: 'loss',
                  },
                  {
                        title: 'Battles',
                        dataIndex: 'battles',
                        key: 'battles',
                  }
            ];
                
            const data = [
                  {
                    "key": 1,
                    "king": 'John Brown',
                    "rating": 32,
                    "wins": 13,
                    "loss": 5,
                    "battles": 45
                  },
                  {
                        'key': 2,
                        'king': 'Robb Stark',
                        'rating': 997.369954236588,
                        'wins': 8,
                        'loss': 11,
                        'battles': 19
                  }, {
                        'key': 3,
                        'king': 'Balon/Euron Greyjoy',
                        'rating': 1015.9922908825638,
                        'wins': 5,
                        'loss': 2,
                        'battles': 7
                  }, {
                        'key': 4,
                        'king': 'Stannis Baratheon',
                        'rating': 997.8014110416522,
                        'wins': 1,
                        'loss': 1,
                        'battles': 2
                  }, {
                        'key': 5,
                        'king': 'Renly Baratheon',
                        'rating': 984.0,
                        'wins': 0,
                        'loss': 1,
                        'battles': 1
                  }
            ];
                
            return (
                <div>
                      <Table columns={columns} dataSource={data} />
                </div>
            );
      }
}

export default BattleStatsTable



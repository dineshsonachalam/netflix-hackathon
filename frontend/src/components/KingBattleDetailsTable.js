import React from 'react';
import { Table, Tag, Space } from 'antd';

class KingBattleDetailsTable extends React.Component {
      render() {
            const columns = [
                  {
                        title: 'Year',
                        dataIndex: 'year',
                        key: 'year',
                        render: text => <a>{text}</a>,
                  },
                  {
                        title: 'Role',
                        dataIndex: 'role',
                        key: 'role',
                  },
                  {
                        title: 'Opponent',
                        dataIndex: 'opponent',
                        key: 'opponent',
                  },
                  {
                        title: 'Battle Outcome',
                        dataIndex: 'battle_outcome',
                        key: 'battle_outcome',
                  },
                  {
                        title: 'Rating',
                        dataIndex: 'rating',
                        key: 'rating',
                  }
            ];
                
            const data =  [
                  {
                      "key": 1,
                      "year": 298,
                      "role": "Attacker",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Win",
                      "rating": 1016.0
                  },
                  {
                      "key": 2,
                      "year": 298,
                      "role": "Attacker",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Win",
                      "rating": 1030.5304984710244
                  },
                  {
                      "key": 3,
                      "year": 298,
                      "role": "Attacker",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Win",
                      "rating": 1043.747133633611
                  },
                  {
                      "key": 4,
                      "year": 298,
                      "role": "Defender",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Win",
                      "rating": 1055.8009426289977
                  },
                  {
                      "key": 5,
                      "year": 298,
                      "role": "Defender",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Loss",
                      "rating": 1034.8312456204
                  },
                  {
                      "key": 6,
                      "year": 298,
                      "role": "Defender",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Loss",
                      "rating": 1015.6654796209059
                  },
                  {
                      "key": 7,
                      "year": 298,
                      "role": "Attacker",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Win",
                      "rating": 1030.2265340285246
                  },
                  {
                      "key": 8,
                      "year": 299,
                      "role": "Attacker",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Win",
                      "rating": 1042.0669707696513
                  },
                  {
                      "key": 9,
                      "year": 299,
                      "role": "Defender",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Loss",
                      "rating": 1020.9097899725217
                  },
                  {
                      "key": 10,
                      "year": 299,
                      "role": "Attacker",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Loss",
                      "rating": 1001.5608602829274
                  },
                  {
                      "key": 11,
                      "year": 299,
                      "role": "Defender",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Loss",
                      "rating": 983.9492836527229
                  },
                  {
                      "key": 12,
                      "year": 299,
                      "role": "Defender",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Loss",
                      "rating": 967.9543098187438
                  },
                  {
                      "key": 13,
                      "year": 299,
                      "role": "Defender",
                      "opponent": "Stannis Baratheon",
                      "battle_outcome": "Win",
                      "rating": 986.1528987770917
                  },
                  {
                      "key": 14,
                      "year": 299,
                      "role": "Defender",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Loss",
                      "rating": 970.7926991412565
                  },
                  {
                      "key": 15,
                      "year": 299,
                      "role": "Defender",
                      "opponent": "Robb Stark",
                      "battle_outcome": "Win",
                      "rating": 988.8363438391959
                  }
            ];
                
            return (
                <div>
                      <Table columns={columns} dataSource={data} />
                </div>
            );
      }
}

export default KingBattleDetailsTable



import requests
import json

def test_battles():
    url = "http://0.0.0.0:8084/battles"
    response = requests.request("GET", url, headers={}, data={})    
    assert response.status_code == 200
    response = response.json()
    expected_response = {
        "info": [
            {
                "key": 3,
                "king": "Balon/Euron Greyjoy",
                "rating": 1031.9923,
                "wins": 4,
                "loss": 1,
                "battles": 5,
                "rank": 1
            },
            {
                "key": 4,
                "king": "Stannis Baratheon",
                "rating": 997.80141,
                "wins": 1,
                "loss": 1,
                "battles": 2,
                "rank": 2
            },
            {
                "key": 2,
                "king": "Robb Stark",
                "rating": 997.36995,
                "wins": 8,
                "loss": 11,
                "battles": 19,
                "rank": 3
            },
            {
                "key": 1,
                "king": "Joffrey/Tommen Baratheon",
                "rating": 988.83634,
                "wins": 8,
                "loss": 7,
                "battles": 15,
                "rank": 4
            },
            {
                "key": 5,
                "king": "Renly Baratheon",
                "rating": 984.0,
                "wins": 0,
                "loss": 1,
                "battles": 1,
                "rank": 5
            }
        ],
        "win_loss_data": [
            {
                "name": "Total Battles",
                "king": "Joffrey/Tommen Baratheon",
                "value": 15
            },
            {
                "name": "Total Wins",
                "king": "Joffrey/Tommen Baratheon",
                "value": 8
            },
            {
                "name": "Total Loss",
                "king": "Joffrey/Tommen Baratheon",
                "value": 7
            },
            {
                "name": "Total Battles",
                "king": "Robb Stark",
                "value": 19
            },
            {
                "name": "Total Wins",
                "king": "Robb Stark",
                "value": 8
            },
            {
                "name": "Total Loss",
                "king": "Robb Stark",
                "value": 11
            },
            {
                "name": "Total Battles",
                "king": "Balon/Euron Greyjoy",
                "value": 5
            },
            {
                "name": "Total Wins",
                "king": "Balon/Euron Greyjoy",
                "value": 4
            },
            {
                "name": "Total Loss",
                "king": "Balon/Euron Greyjoy",
                "value": 1
            },
            {
                "name": "Total Battles",
                "king": "Stannis Baratheon",
                "value": 2
            },
            {
                "name": "Total Wins",
                "king": "Stannis Baratheon",
                "value": 1
            },
            {
                "name": "Total Loss",
                "king": "Stannis Baratheon",
                "value": 1
            },
            {
                "name": "Total Battles",
                "king": "Renly Baratheon",
                "value": 1
            },
            {
                "name": "Total Wins",
                "king": "Renly Baratheon",
                "value": 0
            },
            {
                "name": "Total Loss",
                "king": "Renly Baratheon",
                "value": 1
            }
        ],
        "stats": {
            "Joffrey/Tommen Baratheon": {
                "wins": 8,
                "battles": 15,
                "loss": 7,
                "rating": 988.83634,
                "battle_details": [
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
                        "rating": 1030.5305
                    },
                    {
                        "key": 3,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1043.74714
                    },
                    {
                        "key": 4,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1055.80095
                    },
                    {
                        "key": 5,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1034.83125
                    },
                    {
                        "key": 6,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1015.66548
                    },
                    {
                        "key": 7,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1030.22653
                    },
                    {
                        "key": 8,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1042.06697
                    },
                    {
                        "key": 9,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1020.90979
                    },
                    {
                        "key": 10,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1001.56086
                    },
                    {
                        "key": 11,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 983.94928
                    },
                    {
                        "key": 12,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 967.95431
                    },
                    {
                        "key": 13,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Win",
                        "rating": 986.1529
                    },
                    {
                        "key": 14,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 970.7927
                    },
                    {
                        "key": 15,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 988.83634
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 53.33333
                    },
                    {
                        "type": "Loss",
                        "value": 46.66667
                    }
                ],
                "rating_info": [
                    {
                        "battle": 1,
                        "rating": 1016.0
                    },
                    {
                        "battle": 2,
                        "rating": 1030.5305
                    },
                    {
                        "battle": 3,
                        "rating": 1043.74714
                    },
                    {
                        "battle": 4,
                        "rating": 1055.80095
                    },
                    {
                        "battle": 5,
                        "rating": 1034.83125
                    },
                    {
                        "battle": 6,
                        "rating": 1015.66548
                    },
                    {
                        "battle": 7,
                        "rating": 1030.22653
                    },
                    {
                        "battle": 8,
                        "rating": 1042.06697
                    },
                    {
                        "battle": 9,
                        "rating": 1020.90979
                    },
                    {
                        "battle": 10,
                        "rating": 1001.56086
                    },
                    {
                        "battle": 11,
                        "rating": 983.94928
                    },
                    {
                        "battle": 12,
                        "rating": 967.95431
                    },
                    {
                        "battle": 13,
                        "rating": 986.1529
                    },
                    {
                        "battle": 14,
                        "rating": 970.7927
                    },
                    {
                        "battle": 15,
                        "rating": 988.83634
                    }
                ]
            },
            "Robb Stark": {
                "wins": 8,
                "battles": 19,
                "loss": 11,
                "rating": 997.36995,
                "battle_details": [
                    {
                        "key": 1,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 984.0
                    },
                    {
                        "key": 2,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 969.4695
                    },
                    {
                        "key": 3,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 956.25286
                    },
                    {
                        "key": 4,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 944.19905
                    },
                    {
                        "key": 5,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 965.16875
                    },
                    {
                        "key": 6,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 984.33452
                    },
                    {
                        "key": 7,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 969.77347
                    },
                    {
                        "key": 8,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 955.16195
                    },
                    {
                        "key": 9,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 941.87329
                    },
                    {
                        "key": 10,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 929.75595
                    },
                    {
                        "key": 11,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Win",
                        "rating": 950.66981
                    },
                    {
                        "key": 12,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 937.78117
                    },
                    {
                        "key": 13,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 925.94073
                    },
                    {
                        "key": 14,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 947.09791
                    },
                    {
                        "key": 15,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 966.44684
                    },
                    {
                        "key": 16,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 984.05842
                    },
                    {
                        "key": 17,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1000.05339
                    },
                    {
                        "key": 18,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1015.41359
                    },
                    {
                        "key": 19,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 997.36995
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 42.10526
                    },
                    {
                        "type": "Loss",
                        "value": 57.89474
                    }
                ],
                "rating_info": [
                    {
                        "battle": 1,
                        "rating": 984.0
                    },
                    {
                        "battle": 2,
                        "rating": 969.4695
                    },
                    {
                        "battle": 3,
                        "rating": 956.25286
                    },
                    {
                        "battle": 4,
                        "rating": 944.19905
                    },
                    {
                        "battle": 5,
                        "rating": 965.16875
                    },
                    {
                        "battle": 6,
                        "rating": 984.33452
                    },
                    {
                        "battle": 7,
                        "rating": 969.77347
                    },
                    {
                        "battle": 8,
                        "rating": 955.16195
                    },
                    {
                        "battle": 9,
                        "rating": 941.87329
                    },
                    {
                        "battle": 10,
                        "rating": 929.75595
                    },
                    {
                        "battle": 11,
                        "rating": 950.66981
                    },
                    {
                        "battle": 12,
                        "rating": 937.78117
                    },
                    {
                        "battle": 13,
                        "rating": 925.94073
                    },
                    {
                        "battle": 14,
                        "rating": 947.09791
                    },
                    {
                        "battle": 15,
                        "rating": 966.44684
                    },
                    {
                        "battle": 16,
                        "rating": 984.05842
                    },
                    {
                        "battle": 17,
                        "rating": 1000.05339
                    },
                    {
                        "battle": 18,
                        "rating": 1015.41359
                    },
                    {
                        "battle": 19,
                        "rating": 997.36995
                    }
                ]
            },
            "Balon/Euron Greyjoy": {
                "wins": 4,
                "battles": 5,
                "loss": 1,
                "rating": 1031.9923,
                "battle_details": [
                    {
                        "key": 1,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1014.61152
                    },
                    {
                        "key": 2,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1027.90018
                    },
                    {
                        "key": 3,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1040.01752
                    },
                    {
                        "key": 4,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1019.10366
                    },
                    {
                        "key": 5,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1031.9923
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 80.0
                    },
                    {
                        "type": "Loss",
                        "value": 20.0
                    }
                ],
                "rating_info": [
                    {
                        "battle": 1,
                        "rating": 1014.61152
                    },
                    {
                        "battle": 2,
                        "rating": 1027.90018
                    },
                    {
                        "battle": 3,
                        "rating": 1040.01752
                    },
                    {
                        "battle": 4,
                        "rating": 1019.10366
                    },
                    {
                        "battle": 5,
                        "rating": 1031.9923
                    }
                ]
            },
            "Stannis Baratheon": {
                "wins": 1,
                "battles": 2,
                "loss": 1,
                "rating": 997.80141,
                "battle_details": [
                    {
                        "key": 1,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Renly Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1016.0
                    },
                    {
                        "key": 2,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 997.80141
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 50.0
                    },
                    {
                        "type": "Loss",
                        "value": 50.0
                    }
                ],
                "rating_info": [
                    {
                        "battle": 1,
                        "rating": 1016.0
                    },
                    {
                        "battle": 2,
                        "rating": 997.80141
                    }
                ]
            },
            "Renly Baratheon": {
                "wins": 0,
                "battles": 1,
                "loss": 1,
                "rating": 984.0,
                "battle_details": [
                    {
                        "key": 1,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 984.0
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 0.0
                    },
                    {
                        "type": "Loss",
                        "value": 100.0
                    }
                ],
                "rating_info": [
                    {
                        "battle": 1,
                        "rating": 984.0
                    }
                ]
            }
        }
    }
    assert len(response) == len(expected_response)
    assert all([a == b for a, b in zip(response, expected_response)])
    print(all([a == b for a, b in zip(response, expected_response)]))


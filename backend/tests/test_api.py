import requests
import json

def test_battles():
    url = "http://0.0.0.0:8001/battles"
    response = requests.request("GET", url, headers={}, data={})    
    assert response.status_code == 200
    response = response.json()
    expected_response = {
        "info": [
            {
                "key": 3,
                "king": "Balon/Euron Greyjoy",
                "rating": 1049.86133,
                "wins": 12,
                "loss": 6,
                "battles": 18,
                "rank": 1
            },
            {
                "key": 1,
                "king": "Joffrey/Tommen Baratheon",
                "rating": 1042.30656,
                "wins": 32,
                "loss": 22,
                "battles": 54,
                "rank": 2
            },
            {
                "key": 6,
                "king": "Mance Rayder",
                "rating": 1030.59426,
                "wins": 2,
                "loss": 0,
                "battles": 2,
                "rank": 3
            },
            {
                "key": 4,
                "king": "Stannis Baratheon",
                "rating": 983.07423,
                "wins": 6,
                "loss": 8,
                "battles": 14,
                "rank": 4
            },
            {
                "key": 5,
                "king": "Renly Baratheon",
                "rating": 968.22248,
                "wins": 0,
                "loss": 2,
                "battles": 2,
                "rank": 5
            },
            {
                "key": 2,
                "king": "Robb Stark",
                "rating": 956.31079,
                "wins": 18,
                "loss": 30,
                "battles": 48,
                "rank": 6
            }
        ],
        "win_loss_data": [
            {
                "name": "Total Battles",
                "king": "Joffrey/Tommen Baratheon",
                "value": 54
            },
            {
                "name": "Total Wins",
                "king": "Joffrey/Tommen Baratheon",
                "value": 32
            },
            {
                "name": "Total Loss",
                "king": "Joffrey/Tommen Baratheon",
                "value": 22
            },
            {
                "name": "Total Battles",
                "king": "Robb Stark",
                "value": 48
            },
            {
                "name": "Total Wins",
                "king": "Robb Stark",
                "value": 18
            },
            {
                "name": "Total Loss",
                "king": "Robb Stark",
                "value": 30
            },
            {
                "name": "Total Battles",
                "king": "Balon/Euron Greyjoy",
                "value": 18
            },
            {
                "name": "Total Wins",
                "king": "Balon/Euron Greyjoy",
                "value": 12
            },
            {
                "name": "Total Loss",
                "king": "Balon/Euron Greyjoy",
                "value": 6
            },
            {
                "name": "Total Battles",
                "king": "Stannis Baratheon",
                "value": 14
            },
            {
                "name": "Total Wins",
                "king": "Stannis Baratheon",
                "value": 6
            },
            {
                "name": "Total Loss",
                "king": "Stannis Baratheon",
                "value": 8
            },
            {
                "name": "Total Battles",
                "king": "Renly Baratheon",
                "value": 2
            },
            {
                "name": "Total Wins",
                "king": "Renly Baratheon",
                "value": 0
            },
            {
                "name": "Total Loss",
                "king": "Renly Baratheon",
                "value": 2
            },
            {
                "name": "Total Battles",
                "king": "Mance Rayder",
                "value": 2
            },
            {
                "name": "Total Wins",
                "king": "Mance Rayder",
                "value": 2
            },
            {
                "name": "Total Loss",
                "king": "Mance Rayder",
                "value": 0
            }
        ],
        "stats": {
            "Joffrey/Tommen Baratheon": {
                "wins": 32,
                "battles": 54,
                "loss": 22,
                "rating": 1042.30656,
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
                    },
                    {
                        "key": 16,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1005.22925
                    },
                    {
                        "key": 17,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "",
                        "battle_outcome": "Win",
                        "rating": 1020.98845
                    },
                    {
                        "key": 18,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1035.15396
                    },
                    {
                        "key": 19,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1016.04665
                    },
                    {
                        "key": 20,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Win",
                        "rating": 1032.78046
                    },
                    {
                        "key": 21,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 1015.17165
                    },
                    {
                        "key": 22,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 999.17921
                    },
                    {
                        "key": 23,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1015.19095
                    },
                    {
                        "key": 24,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1029.73201
                    },
                    {
                        "key": 25,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1043.72497
                    },
                    {
                        "key": 26,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1056.46478
                    },
                    {
                        "key": 27,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 1036.51473
                    },
                    {
                        "key": 28,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1049.01127
                    },
                    {
                        "key": 29,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1060.43085
                    },
                    {
                        "key": 30,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1070.90401
                    },
                    {
                        "key": 31,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1080.54598
                    },
                    {
                        "key": 32,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1057.45699
                    },
                    {
                        "key": 33,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1036.17279
                    },
                    {
                        "key": 34,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1048.69933
                    },
                    {
                        "key": 35,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1059.22119
                    },
                    {
                        "key": 36,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1036.90594
                    },
                    {
                        "key": 37,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1016.40796
                    },
                    {
                        "key": 38,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 997.69978
                    },
                    {
                        "key": 39,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 980.68972
                    },
                    {
                        "key": 40,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Win",
                        "rating": 997.7895
                    },
                    {
                        "key": 41,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 981.55732
                    },
                    {
                        "key": 42,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 998.81755
                    },
                    {
                        "key": 43,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1014.49071
                    },
                    {
                        "key": 44,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "",
                        "battle_outcome": "Win",
                        "rating": 1029.10116
                    },
                    {
                        "key": 45,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1042.6767
                    },
                    {
                        "key": 46,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1023.04732
                    },
                    {
                        "key": 47,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Win",
                        "rating": 1040.45034
                    },
                    {
                        "key": 48,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 1023.38591
                    },
                    {
                        "key": 49,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 1007.89143
                    },
                    {
                        "key": 50,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1023.14633
                    },
                    {
                        "key": 51,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1037.00852
                    },
                    {
                        "key": 52,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1050.50073
                    },
                    {
                        "key": 53,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1062.79775
                    },
                    {
                        "key": 54,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 1042.30656
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 59.25926
                    },
                    {
                        "type": "Loss",
                        "value": 40.74074
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
                    },
                    {
                        "battle": 16,
                        "rating": 1005.22925
                    },
                    {
                        "battle": 17,
                        "rating": 1020.98845
                    },
                    {
                        "battle": 18,
                        "rating": 1035.15396
                    },
                    {
                        "battle": 19,
                        "rating": 1016.04665
                    },
                    {
                        "battle": 20,
                        "rating": 1032.78046
                    },
                    {
                        "battle": 21,
                        "rating": 1015.17165
                    },
                    {
                        "battle": 22,
                        "rating": 999.17921
                    },
                    {
                        "battle": 23,
                        "rating": 1015.19095
                    },
                    {
                        "battle": 24,
                        "rating": 1029.73201
                    },
                    {
                        "battle": 25,
                        "rating": 1043.72497
                    },
                    {
                        "battle": 26,
                        "rating": 1056.46478
                    },
                    {
                        "battle": 27,
                        "rating": 1036.51473
                    },
                    {
                        "battle": 28,
                        "rating": 1049.01127
                    },
                    {
                        "battle": 29,
                        "rating": 1060.43085
                    },
                    {
                        "battle": 30,
                        "rating": 1070.90401
                    },
                    {
                        "battle": 31,
                        "rating": 1080.54598
                    },
                    {
                        "battle": 32,
                        "rating": 1057.45699
                    },
                    {
                        "battle": 33,
                        "rating": 1036.17279
                    },
                    {
                        "battle": 34,
                        "rating": 1048.69933
                    },
                    {
                        "battle": 35,
                        "rating": 1059.22119
                    },
                    {
                        "battle": 36,
                        "rating": 1036.90594
                    },
                    {
                        "battle": 37,
                        "rating": 1016.40796
                    },
                    {
                        "battle": 38,
                        "rating": 997.69978
                    },
                    {
                        "battle": 39,
                        "rating": 980.68972
                    },
                    {
                        "battle": 40,
                        "rating": 997.7895
                    },
                    {
                        "battle": 41,
                        "rating": 981.55732
                    },
                    {
                        "battle": 42,
                        "rating": 998.81755
                    },
                    {
                        "battle": 43,
                        "rating": 1014.49071
                    },
                    {
                        "battle": 44,
                        "rating": 1029.10116
                    },
                    {
                        "battle": 45,
                        "rating": 1042.6767
                    },
                    {
                        "battle": 46,
                        "rating": 1023.04732
                    },
                    {
                        "battle": 47,
                        "rating": 1040.45034
                    },
                    {
                        "battle": 48,
                        "rating": 1023.38591
                    },
                    {
                        "battle": 49,
                        "rating": 1007.89143
                    },
                    {
                        "battle": 50,
                        "rating": 1023.14633
                    },
                    {
                        "battle": 51,
                        "rating": 1037.00852
                    },
                    {
                        "battle": 52,
                        "rating": 1050.50073
                    },
                    {
                        "battle": 53,
                        "rating": 1062.79775
                    },
                    {
                        "battle": 54,
                        "rating": 1042.30656
                    }
                ]
            },
            "Robb Stark": {
                "wins": 18,
                "battles": 48,
                "loss": 30,
                "rating": 956.31079,
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
                    },
                    {
                        "key": 20,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 980.97704
                    },
                    {
                        "key": 21,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 966.81153
                    },
                    {
                        "key": 22,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 985.91884
                    },
                    {
                        "key": 23,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 971.92588
                    },
                    {
                        "key": 24,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 959.18607
                    },
                    {
                        "key": 25,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 946.68953
                    },
                    {
                        "key": 26,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 935.26995
                    },
                    {
                        "key": 27,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 924.79679
                    },
                    {
                        "key": 28,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 915.15482
                    },
                    {
                        "key": 29,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 938.24381
                    },
                    {
                        "key": 30,
                        "year": 298,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 959.52801
                    },
                    {
                        "key": 31,
                        "year": 298,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 947.00147
                    },
                    {
                        "key": 32,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 934.81037
                    },
                    {
                        "key": 33,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 923.65939
                    },
                    {
                        "key": 34,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 913.42209
                    },
                    {
                        "key": 35,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Win",
                        "rating": 935.98741
                    },
                    {
                        "key": 36,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Loss",
                        "rating": 924.73778
                    },
                    {
                        "key": 37,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 914.21592
                    },
                    {
                        "key": 38,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 936.53117
                    },
                    {
                        "key": 39,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 957.02915
                    },
                    {
                        "key": 40,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 975.73733
                    },
                    {
                        "key": 41,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 992.74739
                    },
                    {
                        "key": 42,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1008.97957
                    },
                    {
                        "key": 43,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 991.71934
                    },
                    {
                        "key": 44,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 976.04618
                    },
                    {
                        "key": 45,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 962.47064
                    },
                    {
                        "key": 46,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 982.10002
                    },
                    {
                        "key": 47,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 968.60781
                    },
                    {
                        "key": 48,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 956.31079
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 37.5
                    },
                    {
                        "type": "Loss",
                        "value": 62.5
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
                    },
                    {
                        "battle": 20,
                        "rating": 980.97704
                    },
                    {
                        "battle": 21,
                        "rating": 966.81153
                    },
                    {
                        "battle": 22,
                        "rating": 985.91884
                    },
                    {
                        "battle": 23,
                        "rating": 971.92588
                    },
                    {
                        "battle": 24,
                        "rating": 959.18607
                    },
                    {
                        "battle": 25,
                        "rating": 946.68953
                    },
                    {
                        "battle": 26,
                        "rating": 935.26995
                    },
                    {
                        "battle": 27,
                        "rating": 924.79679
                    },
                    {
                        "battle": 28,
                        "rating": 915.15482
                    },
                    {
                        "battle": 29,
                        "rating": 938.24381
                    },
                    {
                        "battle": 30,
                        "rating": 959.52801
                    },
                    {
                        "battle": 31,
                        "rating": 947.00147
                    },
                    {
                        "battle": 32,
                        "rating": 934.81037
                    },
                    {
                        "battle": 33,
                        "rating": 923.65939
                    },
                    {
                        "battle": 34,
                        "rating": 913.42209
                    },
                    {
                        "battle": 35,
                        "rating": 935.98741
                    },
                    {
                        "battle": 36,
                        "rating": 924.73778
                    },
                    {
                        "battle": 37,
                        "rating": 914.21592
                    },
                    {
                        "battle": 38,
                        "rating": 936.53117
                    },
                    {
                        "battle": 39,
                        "rating": 957.02915
                    },
                    {
                        "battle": 40,
                        "rating": 975.73733
                    },
                    {
                        "battle": 41,
                        "rating": 992.74739
                    },
                    {
                        "battle": 42,
                        "rating": 1008.97957
                    },
                    {
                        "battle": 43,
                        "rating": 991.71934
                    },
                    {
                        "battle": 44,
                        "rating": 976.04618
                    },
                    {
                        "battle": 45,
                        "rating": 962.47064
                    },
                    {
                        "battle": 46,
                        "rating": 982.10002
                    },
                    {
                        "battle": 47,
                        "rating": 968.60781
                    },
                    {
                        "battle": 48,
                        "rating": 956.31079
                    }
                ]
            },
            "Balon/Euron Greyjoy": {
                "wins": 12,
                "battles": 18,
                "loss": 6,
                "rating": 1049.86133,
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
                    },
                    {
                        "key": 6,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 1015.25849
                    },
                    {
                        "key": 7,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 997.7271
                    },
                    {
                        "key": 8,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1015.33591
                    },
                    {
                        "key": 9,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1031.32835
                    },
                    {
                        "key": 10,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1043.51945
                    },
                    {
                        "key": 11,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1054.67043
                    },
                    {
                        "key": 12,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1064.90773
                    },
                    {
                        "key": 13,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Loss",
                        "rating": 1042.34241
                    },
                    {
                        "key": 14,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Robb Stark",
                        "battle_outcome": "Win",
                        "rating": 1053.59204
                    },
                    {
                        "key": 15,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 1036.18902
                    },
                    {
                        "key": 16,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 1017.30242
                    },
                    {
                        "key": 17,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1034.36685
                    },
                    {
                        "key": 18,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1049.86133
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 66.66667
                    },
                    {
                        "type": "Loss",
                        "value": 33.33333
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
                    },
                    {
                        "battle": 6,
                        "rating": 1015.25849
                    },
                    {
                        "battle": 7,
                        "rating": 997.7271
                    },
                    {
                        "battle": 8,
                        "rating": 1015.33591
                    },
                    {
                        "battle": 9,
                        "rating": 1031.32835
                    },
                    {
                        "battle": 10,
                        "rating": 1043.51945
                    },
                    {
                        "battle": 11,
                        "rating": 1054.67043
                    },
                    {
                        "battle": 12,
                        "rating": 1064.90773
                    },
                    {
                        "battle": 13,
                        "rating": 1042.34241
                    },
                    {
                        "battle": 14,
                        "rating": 1053.59204
                    },
                    {
                        "battle": 15,
                        "rating": 1036.18902
                    },
                    {
                        "battle": 16,
                        "rating": 1017.30242
                    },
                    {
                        "battle": 17,
                        "rating": 1034.36685
                    },
                    {
                        "battle": 18,
                        "rating": 1049.86133
                    }
                ]
            },
            "Stannis Baratheon": {
                "wins": 6,
                "battles": 14,
                "loss": 8,
                "rating": 983.07423,
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
                    },
                    {
                        "key": 3,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Mance Rayder",
                        "battle_outcome": "Loss",
                        "rating": 981.90266
                    },
                    {
                        "key": 4,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Win",
                        "rating": 999.43405
                    },
                    {
                        "key": 5,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 983.42231
                    },
                    {
                        "key": 6,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 968.88125
                    },
                    {
                        "key": 7,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 988.8313
                    },
                    {
                        "key": 8,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Renly Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1004.60882
                    },
                    {
                        "key": 9,
                        "year": 299,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 987.50904
                    },
                    {
                        "key": 10,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Mance Rayder",
                        "battle_outcome": "Loss",
                        "rating": 972.81353
                    },
                    {
                        "key": 11,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Balon/Euron Greyjoy",
                        "battle_outcome": "Win",
                        "rating": 991.70013
                    },
                    {
                        "key": 12,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 976.44523
                    },
                    {
                        "key": 13,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 962.58304
                    },
                    {
                        "key": 14,
                        "year": 300,
                        "role": "Attacker",
                        "opponent": "Joffrey/Tommen Baratheon",
                        "battle_outcome": "Win",
                        "rating": 983.07423
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 42.85714
                    },
                    {
                        "type": "Loss",
                        "value": 57.14286
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
                    },
                    {
                        "battle": 3,
                        "rating": 981.90266
                    },
                    {
                        "battle": 4,
                        "rating": 999.43405
                    },
                    {
                        "battle": 5,
                        "rating": 983.42231
                    },
                    {
                        "battle": 6,
                        "rating": 968.88125
                    },
                    {
                        "battle": 7,
                        "rating": 988.8313
                    },
                    {
                        "battle": 8,
                        "rating": 1004.60882
                    },
                    {
                        "battle": 9,
                        "rating": 987.50904
                    },
                    {
                        "battle": 10,
                        "rating": 972.81353
                    },
                    {
                        "battle": 11,
                        "rating": 991.70013
                    },
                    {
                        "battle": 12,
                        "rating": 976.44523
                    },
                    {
                        "battle": 13,
                        "rating": 962.58304
                    },
                    {
                        "battle": 14,
                        "rating": 983.07423
                    }
                ]
            },
            "Renly Baratheon": {
                "wins": 0,
                "battles": 2,
                "loss": 2,
                "rating": 968.22248,
                "battle_details": [
                    {
                        "key": 1,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 984.0
                    },
                    {
                        "key": 2,
                        "year": 299,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Loss",
                        "rating": 968.22248
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
                    },
                    {
                        "battle": 2,
                        "rating": 968.22248
                    }
                ]
            },
            "Mance Rayder": {
                "wins": 2,
                "battles": 2,
                "loss": 0,
                "rating": 1030.59426,
                "battle_details": [
                    {
                        "key": 1,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1015.89875
                    },
                    {
                        "key": 2,
                        "year": 300,
                        "role": "Defender",
                        "opponent": "Stannis Baratheon",
                        "battle_outcome": "Win",
                        "rating": 1030.59426
                    }
                ],
                "win_loss_stats": [
                    {
                        "type": "Win",
                        "value": 100.0
                    },
                    {
                        "type": "Loss",
                        "value": 0.0
                    }
                ],
                "rating_info": [
                    {
                        "battle": 1,
                        "rating": 1015.89875
                    },
                    {
                        "battle": 2,
                        "rating": 1030.59426
                    }
                ]
            }
        }
    }
    assert len(response) == len(expected_response)
    assert all([a == b for a, b in zip(response, expected_response)])
    print(all([a == b for a, b in zip(response, expected_response)]))


let expected_kings_data = {
    1: {
        "key": 3,
        "king": "Balon/Euron Greyjoy",
        "rating": 1031.9923,
        "wins": 4,
        "loss": 1,
        "battles": 5,
        "rank": 1
    },
    2: {
        "key": 4,
        "king": "Stannis Baratheon",
        "rating": 997.80141,
        "wins": 1,
        "loss": 1,
        "battles": 2,
        "rank": 2
    },
    3: {
        "key": 2,
        "king": "Robb Stark",
        "rating": 997.36995,
        "wins": 8,
        "loss": 11,
        "battles": 19,
        "rank": 3
    },
    4: {
        "key": 1,
        "king": "Joffrey/Tommen Baratheon",
        "rating": 988.83634,
        "wins": 8,
        "loss": 7,
        "battles": 15,
        "rank": 4
    },
    5: {
        "key": 5,
        "king": "Renly Baratheon",
        "rating": 984.0,
        "wins": 0,
        "loss": 1,
        "battles": 1,
        "rank": 5
    }
}
let total_kings = Object.keys(expected_kings_data).length

for (var index=1; index < total_kings+1; index++) {   
    // console.log(expected_kings_data[index]);
    let table_key = expected_kings_data[index]["key"]
    let expected_rank =  expected_kings_data[index]["rank"].toString();
    console.log(expected_rank)
}



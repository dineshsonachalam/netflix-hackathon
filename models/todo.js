var connection = require('../connection');

var config = require('../battles_table.json'); // just use require and the path to your JSON file
var config2 = require('../rating_table.json'); // just use require and the path to your JSON file
var config3 = require('../test_table.json'); // just use require and the path to your JSON file
var fs = require('fs');
var fileName = '../rating_table.json';
var counter = 0;
function Todo()
{
    this.get = function(res)
  {
        connection.acquire(function(err, con)
        {




            con.query('select * from battles', function(err, result)
            {
              counter = Object.keys(result).length;
          //    console.log(counter);

/*
              var objs0 = [];
              var objs1 = [];
              var objs2 = [];
              var objs3 = [];
              var objs4 = [];
              var objs5 = [];
*/
                for(var key in result)
              {

                /*
                for (var i = 0; i <38; i++) {



                  objs.push({
                  "response": key,goals: [
                                                  {
                                                    battle_number: config[i].battle_number ,
                                                    attacker_king: config[i].attacker_king,
                                                    name:config[i].name,
                                                    year:config[i].year,
                                                    attacker_outcome:config[i].attacker_outcome,
                                                  }
                                         ]

                  });
                  }


                  fs.writeFile('test_table.json', JSON.stringify(objs), function (err)
                  {
                      if (err) throw err;
                        console.log('Saved!');
                  });
                  */

              }
              /*
              for(var i=0;i<counter;i++)
              {

                console.log(config[i].attacker_king);
              }
              */

//create array in javascript for finding the total battle , total_loss , total_wins,rating

              var data1 = new Array(6) ; //creating dynamic array for finding total battle
              var data2 = new Array(6); // total_wins
              var data3 = new Array(6); // total_loss
              var data4 = new Array(6); // total_rating
              for (var i = 0; i < 6; i++) {
                data1[i] = 0; //initally all the values are 0
                data2[i] = 0;
                data3[i] = 0;
                data4[i] = 0;
              }
              var counter1 = 1;
              for(var i=0;i<38;i++)
          {

              // now calculation
                var battles_attacker;
                var battles_defender;
                var wins_attacker;
                var wins_defender;
                var loss_attacker;
                var loss_defender;
                var king1_position=0;
                var king2_position=0;
                var r1;
                var r2;
                var k=32;
                var x; //calculated rating for king 1
                var y;
                var king1 = config[i].attacker_king;
                var king2 = config[i].defender_king;


              for(var j=0;j<6;j++)
              {

                       if( (king1.length>0)  &&  (king1 === config2[j].king) && (data4[j]==0) )
                       {
                          r1 = 400;
                          data1[j]+=1; //for first battle
                          king1_position = j;

                       }
                       else if((king2.length>0)  && (king2 === config2[j].king) && (data4[j]==0)  )
                       {
                         r2 = 400;
                         king2_position = j;
                         data1[j]+=1; //for first battle
                       }
                       else  if((king1.length>0)  && (king1 === config2[j].king) && (data4[j]!=0) )
                       {
                          r1 = data4[j];
                          king1_position = j;
                          data1[j]+=1; //for first battle
                       }
                       else if( (king2.length>0)  && (king2 === config2[j].king) && (data4[j]!=0) )
                       {
                          r2 = data4[j];
                          king2_position = j;
                          data1[j]+=1; //for first battle
                       }

                }
              //now calculating elo rating
              var R1 =Math.pow(10,r1/400);
              var R2 =Math.pow(10,r2/400);
              //2nd step -expected score for each king
              var e1 = R1 /(R1+R2);
              var e2 = R2 /(R1+R2);
              //after battle finishes
              //3rd step
              var s1;
              var s2;

              // data2 --> wins :  data3-->loss
              if(config[i].attacker_outcome =="win") //attacker wins
            {
                s1 = 1;
                s2=0;
                data2[king1_position] += 1; //data2(attacker) wins
                data3[king2_position] += 1; //data3(defender)loss

            }
            else if(config[i].attacker_outcome =="loss")
            {
                s2 =1;
                s1= 0;
                data2[king2_position] += 1; //wins
                data3[king1_position] += 1; //loss
            }
             //4 th step update elo rating for each king
             x = r1 + k*(s1-e1);
             y = r2 + k*(s2-e2);
             //ratings for the attacker_king
             data4[king1_position] = x;
             data4[king2_position] = y;

//             console.log(king1+" "+counter1+" --->"+x);

  //           console.log(king2+" "+counter1+" --->"+y);
    //         console.log("\n");
      //       counter1 +=1;

            }
           console.log("Total Battles");
            for (var i = 0; i < 6; i++)
            {
                console.log(config2[i].king+"     ---> Total Battles ----> "
                +data1[i]+"  Wins---> "
                +data2[i]+"   Loss-------->  "+data3[i]+"   Rating-----> "+data4[i]);
                console.log("\n");
            }

/*
            for(var i=0;i<38;i++)
        {

              var flag1 = 0;
              var flag2 = 0;

            var king1 = config[i].attacker_king;
            var king2 = config[i].defender_king;
            var king1_position;
            var king2_position;

            for(var j=0;j<6;j++)
            {

                              //initial rating for 1st battle
                    if( (king1.length>0)  &&  (king1 == config3[j].king) && flag1==0)
                    {
                      flag1 = 1;
                      king1_position = j;

                      //JSON UPDATE total_wins of attacker and loss of defender
                        console.log("King1 position:"+j+"->"+config[i].battle_number+king1);
                      var data = [];
                      if(j == 0)
                      {
                          data = objs0;
                      }
                      else if (j == 1)
                      {
                          data = objs1;
                      }
                      else if (j == 2)
                      {
                          data = objs2;
                      }
                      else if (j == 3)
                      {
                          data = objs3;
                      }
                      else if (j == 4)
                      {
                          data = objs4;
                          console.log("--------------------------------------");

                      }
                      else if (j == 5)
                      {
                          data = objs5;
                          console.log("--------------------------------------");

                      }

                        data.push({

                                                          "king_type":"attacker",
                                                          "battle_number": config[i].battle_number ,
                                                          "year":config[i].year,
                                                          "name" : config[i].name,
                                                          "defender_king" : config[i].defender_king,
                                                          "attacker_1" :   config[i].attacker_1,
                                                          "attacker_2" : config[i].attacker_2,
                                                          "attacker_3" :config[i].attacker_3,
                                                          "attacker_4" :config[i].attacker_4,
                                                          "defender_1" :config[i].defender_1,
                                                          "defender_2" :config[i].defender_2,
                                                          "defender_3" :config[i].defender_3,
                                                          "defender_4" :config[i].defender_3,
                                                          "attacker_outcome" :config[i].attacker_outcome,
                                                          "battle_type" :config[i].battle_type,
                                                          "major_death" :config[i].major_death,
                                                          "major_capture" :config[i].major_capture,
                                                          "attacker_size" :config[i].attacker_size,
                                                          "defender_size" :config[i].defender_size,
                                                          "attacker_commander" :config[i].attacker_commander,
                                                          "defender_commander" :config[i].defender_commander,
                                                          "summer" :config[i].summer,
                                                          "location" :config[i].location,
                                                          "region" :config[i].region,
                                                          "note" :config[i].note


                        });

                        config3[j].battle_details = data;

                        fs.writeFile('test_table.json', JSON.stringify(config3), function (err) {
                        if (err) return console.log(err);
                    //    console.log(JSON.stringify(config3));
                    //    console.log('writing to ' + "test_table.json");
                        });


                    }
                    else if((king2.length>0)  && (king2 == config3[j].king)  && flag2==0 )
                    {
                      flag2 =1;
                      king2_position = j;
                      console.log("King2 position:"+j+"->"+config[i].battle_number+" "+king2);

                      //JSON UPDATE total_wins of attacker and loss of defender
                      var data = [];
                      if(j == 0)
                      {
                          data = objs0;
                      }
                      else if (j == 1)
                      {
                          data = objs1;
                      }
                      else if (j == 2)
                      {
                          data = objs2;
                      }
                      else if (j == 3)
                      {
                          data = objs3;
                      }
                      else if (j == 4)
                      {
                          data = objs4;
                          console.log("--------------------------------------");
                      }
                      else if (j == 5)
                      {
                          data = objs5;
                          console.log("--------------------------------------");
                      }

                        data.push({

                                                                "king_type":"defender",
                                                                "battle_number": config[i].battle_number ,
                                                                "year":config[i].year,
                                                                "name" : config[i].name,
                                                                "attacker_king" : config[i].attacker_king,
                                                                "attacker_1" :   config[i].attacker_1,
                                                                "attacker_2" : config[i].attacker_2,
                                                                "attacker_3" :config[i].attacker_3,
                                                                "attacker_4" :config[i].attacker_4,
                                                                "defender_1" :config[i].defender_1,
                                                                "defender_2" :config[i].defender_2,
                                                                "defender_3" :config[i].defender_3,
                                                                "defender_4" :config[i].defender_3,
                                                                "attacker_outcome" :config[i].attacker_outcome,
                                                                "battle_type" :config[i].battle_type,
                                                                "major_death" :config[i].major_death,
                                                                "major_capture" :config[i].major_capture,
                                                                "attacker_size" :config[i].attacker_size,
                                                                "defender_size" :config[i].defender_size,
                                                                "attacker_commander" :config[i].attacker_commander,
                                                                "defender_commander" :config[i].defender_commander,
                                                                "summer" :config[i].summer,
                                                                "location" :config[i].location,
                                                                "region" :config[i].region,
                                                                "note" :config[i].note


                        });

                        config3[j].battle_details = data;

                        fs.writeFile('test_table.json', JSON.stringify(config3), function (err) {
                        if (err) return console.log(err);
                      //  console.log(JSON.stringify(config3));
                      //  console.log('writing to ' + "test_table.json");
                        });


                    }

              }

          }

*/


//testing my parent child relationship
/*
for (var i = 0; i < 38; i++)
{
    for (var j = 0; j<6; j++)
    {
      console.log(config2[j].king+" ->"+config[i].battle_number+" "+config[i].attacker_king);
    }
    console.log("\n");
}
*/


              //update a value in a json file and save it through node.js
              /*
              config2[0].king = "Dinesh Sonachalam";
              config2[0].rating = 99;
              config2[4].king = "Niranjan";

              fs.writeFile('rating_table.json', JSON.stringify(config2), function (err) {
              if (err) return console.log(err);
              console.log(JSON.stringify(config2));
              console.log('writing to ' + fileName);
              });
              */


              });


/*
              var data = JSON.parse(body);
              var responseJson = JSON.stringify(data.response);

              var query = connection.query('INSERT INTO rating SET column=?', responseJson, function(err, result) {
                if(err) throw err;
                console.log('data inserted');
              });
*/

//now inserting rating,total_wins,total_loss,total_battles to tester2 table
/*
for (var i = 0; i < 6; i++)
{
  var post = {

                  king : config3[i].king ,
                  rating : config3[i].rating ,
                  total_wins: config3[i].total_wins ,
                  total_loss: config3[i].total_loss ,
                  total_battles: config3[i].total_battles

            };
  con.query('INSERT INTO tester SET ?', post,function(err, result)
  {

    console.log("Value inserted ");

  });

}
*/

              con.query('select * from rating', function(err, result)
              {
                counter = Object.keys(result).length;
            //    console.log(counter);
                  for(var key in result)
                {

                    /*
                    objs.push({king1: result[key].attacker_king,
                               king2: result[key].defender_king,
                               king1_war_status: result[key].attacker_outcome,
                               battle_number: result[key].battle_number
                    });
                    */

                    /*

                    fs.writeFile('rating_table.json', JSON.stringify(result), function (err)
                    {
                        if (err) throw err;
                          console.log('Saved!');
                    });
                    */

                  }

                  res.end(JSON.stringify(config3));
                  con.release();

                });







          });

    };
  }
module.exports = new Todo();

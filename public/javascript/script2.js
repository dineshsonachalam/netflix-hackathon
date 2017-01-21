//console.log(king.length);

function king_Function(sel)
 {




   $(function() {




  $.getJSON('http://localhost:8000/todo', function(data) {

    const obj = data;
    console.log(obj);
     //define variables here


      $.each(data.person, function(i, f) {

         var tblRow = "<tr>" + "<td>" + f.king + "</td>" +
          "<td>" + f.rating + "</td>" + "<td>" + f.total_wins
          + "</td>" + "<td>" + f.total_loss + "</td>" + "<td>" + f.total_battles + "</td>" +  "</tr>"
          $(tblRow).appendTo("#userdata tbody");
    });

    for (var i = 0; i < 6; i++)
    {
      console.log(obj.person[i].king+"\n");
      for (var j = 0; j < obj.person[i].battle_details.length; j++)
      {
         console.log(obj.person[i].battle_details[j].battle_number);
      }
    }


    var option =  sel.options[sel.selectedIndex].value;
    var i = option;

    //Responsively change the images of the king when the function is called
    //I should display the image of the king here
    var image_loc= "";
    if(i == 0)
    {
      document.getElementById('imageDiv')
          .innerHTML = '<img src="/img/img1.jpg"/ class="img-rounded img-responsive">';

           document.getElementById('demo').innerHTML = "Joffrey/Tommen Baratheon";

           var a = obj.person[i].total_battles; //getting battles
           var b = a.toString(); //converting battles to string
           var c= "Total Battles: "
           var res = c.concat(b)

           document.getElementById('demo2').innerHTML = res;

           // for total wins
           var x = obj.person[i].total_wins; //getting battles
           var y = x.toString(); //converting battles to string
           var z= "Total Wins:&nbsp;&nbsp;&nbsp;&nbsp;"
           var res2 = z.concat(x)

           document.getElementById('demo3').innerHTML = res2;

           //for total loss

           var d = obj.person[i].total_loss; //getting battles
           var e = d.toString(); //converting battles to string
           var f= "Total Loss:&nbsp;&nbsp;&nbsp;&nbsp;"
           var res3 = f.concat(e)

           document.getElementById('demo4').innerHTML = res3;


    }
    else if(i == 1)
    {
      document.getElementById('imageDiv')
          .innerHTML = '<img src="/img/img2.png"/ class="img-rounded img-responsive">';
             document.getElementById('demo').innerHTML = "Robb Stark";
             var a = obj.person[i].total_battles; //getting battles
             var b = a.toString(); //converting battles to string
             var c= "Total Battles:"
             var res = c.concat(b)

             document.getElementById('demo2').innerHTML = res;
             // for total wins
             var x = obj.person[i].total_wins; //getting battles
             var y = x.toString(); //converting battles to string
             var z= "Total Wins:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
             var res2 = z.concat(x)

             document.getElementById('demo3').innerHTML = res2;

                        //for total loss

                        var d = obj.person[i].total_loss; //getting battles
                        var e = d.toString(); //converting battles to string
                        var f= "Total Loss:&nbsp;&nbsp;&nbsp;&nbsp;"
                        var res3 = f.concat(e)

                        document.getElementById('demo4').innerHTML = res3;

    }
    else if(i == 2)
    {
      document.getElementById('imageDiv')
          .innerHTML = '<img src="/img/img3.png"/ class="img-rounded img-responsive">';
             document.getElementById('demo').innerHTML = "Balon/Euron Greyjoy";
             var a = obj.person[i].total_battles; //getting battles
             var b = a.toString(); //converting battles to string
             var c= "Total Battles:"
             var res = c.concat(b)

             document.getElementById('demo2').innerHTML = res;
             // for total wins
             var x = obj.person[i].total_wins; //getting battles
             var y = x.toString(); //converting battles to string
             var z= "Total Wins:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
             var res2 = z.concat(x)

             document.getElementById('demo3').innerHTML = res2;

                        //for total loss

                        var d = obj.person[i].total_loss; //getting battles
                        var e = d.toString(); //converting battles to string
                        var f= "Total Loss:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                        var res3 = f.concat(e)

                        document.getElementById('demo4').innerHTML = res3;


    }
    else if(i == 3)
    {
      document.getElementById('imageDiv')
          .innerHTML = '<img src="/img/img4.png"/ class="img-rounded img-responsive">';
       document.getElementById('demo').innerHTML = "Stannis Baratheon";
       var a = obj.person[i].total_battles; //getting battles
       var b = a.toString(); //converting battles to string
       var c= "Total Battles:"
       var res = c.concat(b)

       document.getElementById('demo2').innerHTML = res;
       // for total wins
       var x = obj.person[i].total_wins; //getting battles
       var y = x.toString(); //converting battles to string
       var z= "Total Wins:&nbsp;&nbsp;&nbsp;&nbsp;";
       var res2 = z.concat(x)

       document.getElementById('demo3').innerHTML = res2;

                  //for total loss

                  var d = obj.person[i].total_loss; //getting battles
                  var e = d.toString(); //converting battles to string
                  var f= "Total Loss:&nbsp;&nbsp;&nbsp;&nbsp;"
                  var res3 = f.concat(e)

                  document.getElementById('demo4').innerHTML = res3;


    }
    else if(i == 4)
    {
      document.getElementById('imageDiv')
          .innerHTML = '<img src="/img/img5.png"/ class="img-rounded img-responsive">';
       document.getElementById('demo').innerHTML = "Renly Baratheon";
       var a = obj.person[i].total_battles; //getting battles
       var b = a.toString(); //converting battles to string
       var c= "Total Battles:"
       var res = c.concat(b)

       document.getElementById('demo2').innerHTML = res;
       // for total wins
       var x = obj.person[i].total_wins; //getting battles
       var y = x.toString(); //converting battles to string
       var z= "Total Wins:&nbsp;&nbsp;&nbsp;&nbsp;";
       var res2 = z.concat(x)

       document.getElementById('demo3').innerHTML = res2;

                  //for total loss

                  var d = obj.person[i].total_loss; //getting battles
                  var e = d.toString(); //converting battles to string
                  var f= "Total Loss:&nbsp;&nbsp;&nbsp;&nbsp;"
                  var res3 = f.concat(e)

                  document.getElementById('demo4').innerHTML = res3;

    }
    else if(i == 5)
    {
      document.getElementById('imageDiv')
          .innerHTML = '<img src="/img/img6.jpg"/ class="img-rounded img-responsive">';
       document.getElementById('demo').innerHTML = "Mance Rayder";
       var a = obj.person[i].total_battles; //getting battles
       var b = a.toString(); //converting battles to string
       var c= "Total Battles:"
       var res = c.concat(b)

       document.getElementById('demo2').innerHTML = res;
       // for total wins
       var x = obj.person[i].total_wins; //getting battles
       var y = x.toString(); //converting battles to string
       var z= "Total Wins:&nbsp;&nbsp;&nbsp;&nbsp;";
       var res2 = z.concat(x)

       document.getElementById('demo3').innerHTML = res2;

                  //for total loss

                  var d = obj.person[i].total_loss; //getting battles
                  var e = d.toString(); //converting battles to string
                  var f= "Total Loss:&nbsp;&nbsp;&nbsp;&nbsp;"
                  var res3 = f.concat(e)

                  document.getElementById('demo4').innerHTML = res3;


    }


/*
    document.getElementById('imageDiv')
        .innerHTML = '<img src="/img/img1.jpg"/ class="img-rounded img-responsive">';
*/



            //adding google charts for table

            //// Load Charts and the corechart package (add the chart package before adding any chart)
            google.charts.load('current', {'packages':['table','corechart', 'bar']});

            google.charts.setOnLoadCallback(drawTable1); //function call

            function drawTable1() {


              var data = new google.visualization.DataTable();


                //add data format as string

                 data.addColumn('string', 'king_type');
                 data.addColumn('number', 'battle_number');
                 data.addColumn('number', 'year');
                 data.addColumn('string', 'name');
                 data.addColumn('string', 'enemy_king');
                 data.addColumn('string', 'attacker_1');
                 data.addColumn('string', 'attacker_2');
                 data.addColumn('string', 'attacker_3');
                 data.addColumn('string', 'attacker_4');
                 data.addColumn('string', 'defender_1');
                 data.addColumn('string', 'defender_2');
                 data.addColumn('string', 'defender_3');
                 data.addColumn('string', 'defender_4');
                 data.addColumn('string', 'attacker_outcome');
                 data.addColumn('string', 'battle_type');

                 data.addColumn('number', 'major_death');
                 data.addColumn('number', 'major_capture');

                 data.addColumn('string', 'attacker_size');
                 data.addColumn('string', 'defender_size');

                 data.addColumn('string', 'attacker_commander');
                 data.addColumn('string', 'defender_commander');
                 data.addColumn('string', 'summer');
                 data.addColumn('string', 'location');
                 data.addColumn('string', 'region');
                 data.addColumn('string', 'note');

                 console.log("In function"+obj.person[i].battle_details.length);


                 for (var j = 0; j < obj.person[i].battle_details.length; j++)
  {

              data.addRows([
                [

                  obj.person[i].battle_details[j].king_type,
                   obj.person[i].battle_details[j].battle_number,
                   obj.person[i].battle_details[j].year,
                   obj.person[i].battle_details[j].name,
                   obj.person[i].battle_details[j].enemy_king,
                   obj.person[i].battle_details[j].attacker_1,
                   obj.person[i].battle_details[j].attacker_2,
                   obj.person[i].battle_details[j].attacker_3,
                   obj.person[i].battle_details[j].attacker_4,
                   obj.person[i].battle_details[j].defender_1,
                   obj.person[i].battle_details[j].defender_2,
                   obj.person[i].battle_details[j].defender_3,
                   obj.person[i].battle_details[j].defender_4,
                   obj.person[i].battle_details[j].attacker_outcome,
                   obj.person[i].battle_details[j].battle_type,
                   obj.person[i].battle_details[j].major_death,
                   obj.person[i].battle_details[j].major_capture,
                   obj.person[i].battle_details[j].attacker_size,
                   obj.person[i].battle_details[j].defender_size,

                   obj.person[i].battle_details[j].attacker_commander,
                   obj.person[i].battle_details[j].defender_commander,
                   obj.person[i].battle_details[j].summer,
                   obj.person[i].battle_details[j].location,
                   obj.person[i].battle_details[j].region,
                   obj.person[i].battle_details[j].note

                ]
               ]);
  }

              var table = new google.visualization.Table(document.getElementById('table_div'));

              table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});

          }




  }); //json function end write code above

}); //function ends here





 }

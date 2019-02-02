

    $(function() {




   $.getJSON('http://localhost:8006/todo', function(data) {

     const obj = data;
     console.log(obj);
      //define variables here
      var king = [];
      var rating = [];
      var total_wins = [];
      var total_loss = [];
      var total_battles = [];
      var battle_details = [];

       $.each(data.person, function(i, f) {

          var z = f.battle_details;
          battle_details =z;

          var temp = f.king;
          king.push(temp.toString());

          var temp1 = f.rating;
          rating.push(temp1);

          var temp2 = f.total_wins;
          total_wins.push(temp2);

          var temp3 = f.total_loss;
          total_loss.push(temp3);

          var temp4 = f.total_battles;
          total_battles.push(temp4);


          var tblRow = "<tr>" + "<td>" + f.king + "</td>" +
           "<td>" + f.rating + "</td>" + "<td>" + f.total_wins
           + "</td>" + "<td>" + f.total_loss + "</td>" + "<td>" + f.total_battles + "</td>" +  "</tr>"
           $(tblRow).appendTo("#userdata tbody");
     });


     console.log(king);
     console.log(rating);
     console.log(total_battles);
     console.log(total_loss);
     console.log(king[0]);
     console.log(rating[5]);
     console.log(king.length);
     console.log(battle_details);

     for (var i = 0; i < 6; i++)
     {
       console.log(obj.person[i].king+"\n");
       for (var j = 0; j < obj.person[i].battle_details.length; j++)
       {
          console.log(obj.person[i].battle_details[j].battle_number);
       }
     }

     //adding google charts for table

     //// Load Charts and the corechart package (add the chart package before adding any chart)
     google.charts.load('current', {'packages':['table','corechart', 'bar']});

     google.charts.setOnLoadCallback(drawTable1); //function call

     // Draw the pie chart for total wins of the kings
      google.charts.setOnLoadCallback(drawTable2);

    // Draw the Donut chart for total loss of the kings
      google.charts.setOnLoadCallback(drawTable3);

    // Draw the column chart for the total rating of the kings
      google.charts.setOnLoadCallback(drawTable4);

    // Draw the column chart for displaying total wins,total loss and total battles_defender
     google.charts.setOnLoadCallback(drawTable5);

     function drawTable1() {


       var data = new google.visualization.DataTable();
       data.addColumn('string', 'King');
       data.addColumn('number', 'Rating');
       data.addColumn('number', 'Total Wins');
       data.addColumn('number', 'Total Loss');
       data.addColumn('number', 'Total Battles');
     for (var i = 0; i < 6; i++) {
       data.addRows([
         [king[i],rating[i],total_wins[i],total_loss[i],total_battles[i]]
        ]);


      }
       var table = new google.visualization.Table(document.getElementById('table_div'));

       table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
     }
   //adding google Pie chart for total wins of the king

   function drawTable2() {

          // Create the data table for Sarah's pizza.
          var data = new google.visualization.DataTable();
          data.addColumn('string', 'Kings');
          data.addColumn('number', 'Wins');
          for (var i = 0; i < 6; i++) {
          data.addRows([
            [king[i],total_wins[i]]
          ]);
        }

          // Set options for Sarah's pie chart.
          var options = {title:'Total Winning outcome of the kings',
                         width:600,
                         height:600};

          // Instantiate and draw the chart for Sarah's pizza.
          var chart = new google.visualization.PieChart(document.getElementById('Win_chart_div'));
          chart.draw(data, options);
        }

        function drawTable3() {

          for (var i = 0; i < 6; i++)
    {

        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Kings');
        data.addColumn('number', 'Wins');
        for (var i = 0; i < 6; i++) {
        data.addRows([
          [king[i],total_loss[i]]
        ]);
      }
    }
        var options = {
          title: 'Total Loss percentage of the kings',
          pieHole: 0.4,
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
        chart.draw(data, options);
  }




  function drawTable4() {


    for (var i = 0; i < 6; i++)
{

  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Kings');
  data.addColumn('number', 'Ratings');
  for (var i = 0; i < 6; i++) {
  data.addRows([
    [king[i],rating[i]]
  ]);
}
}


    /*
       var data = new google.visualization.arrayToDataTable([
         ['Galaxy', 'Rating'],
         ['Canis Major Dwarf', 8000],
         ['Sagittarius Dwarf', 24000],
         ['Ursa Major II Dwarf', 30000],
         ['Lg. Magellanic Cloud', 50000],
         ['Bootes I', 60000]
       ]);
*/
       var options = {
         width: 900,
         chart: {
           title: 'Rating of the kings',
           subtitle: 'Total rating achieved by the kings'
         },
         series: {
           0: { axis: 'distance' }, // Bind series 0 to an axis named 'distance'.
        //   1: { axis: 'brightness' } // Bind series 1 to an axis named 'brightness'.
         },
         axes: {
           y: {
             distance: {label: ''}, // Left y-axis.
             brightness: {side: 'right', label: 'apparent magnitude'} // Right y-axis.
           }
         }
       };

     var chart = new google.charts.Bar(document.getElementById('rating_div'));
     chart.draw(data, options);
   };



   function drawTable5() {
     /*
        var data = google.visualization.arrayToDataTable([
          ['Year', 'Sales', 'Expenses', 'Profit'],
          ['2014', 1000, 400, 200],
          ['2015', 1170, 460, 250],
          ['2016', 660, 1120, 300],
          ['2017', 1030, 540, 350]
        ]);
*/

for (var i = 0; i < 6; i++)
{

var data = new google.visualization.DataTable();
data.addColumn('string', 'Kings');
data.addColumn('number', 'Total Battles');
data.addColumn('number', 'Total Wins');
data.addColumn('number', 'Total Loss');
for (var i = 0; i < 6; i++) {
data.addRows([
[ king[i],total_battles[i],total_wins[i],total_loss[i] ]
]);
}
}


        var options = {
          chart: {
            title: 'Battle Statistics',
            subtitle: 'Total battles,Total wins,Total battles',
          }
        };

        var chart = new google.charts.Bar(document.getElementById('columnchart_material'));

        chart.draw(data, options);
      }

   }); //json function end write code above

}); 

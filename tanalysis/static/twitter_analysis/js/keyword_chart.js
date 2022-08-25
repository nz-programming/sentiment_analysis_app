// ('#exampleModal').on('shown.bs.modal', function (event) {
//     console.log("hogehgehoge")
    // const create_date =  dataset["create_date"];
    // const sentiment_score = dataset["average_polality"]

    // chart with chart.js
    var context = document.getElementById("keywordbarChart");
    var myLinekeywordchart  = new Chart(context, {
        type: 'bar',
        data: {
            labels: create_date,
            datasets: [{
                label: 'Daily Average Sentiment Score',
                // data:data.data,
                data:sentiment_score,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255,99,132,1)',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
// });
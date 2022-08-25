function createKeywordChart(index){
    const chart_dataset = dataset["keyword_count"];
    const data_object = JSON.parse(chart_dataset[index]);
    
    const keys = Object.keys(data_object["count"]);
    const values = Object.values(data_object["count"]);

    var context = document.getElementById("keywordbarChart");

    // var keywordchart
    if(document.keywordchart != null){
        console.log(document.keywordchart);
        document.keywordchart.destroy()
    }
    document.keywordchart  = new Chart(context, {
            type: 'bar',
            data: {
                labels: keys,
                datasets: [{
                    label: 'Number of Keyword',
                    data: values,
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
        // console.log(keywordchart);
        // console.log(typeof(keywordchart));
};
/* 

This file create modal content below;
    "sentiment score ranking"
    "number of retweet ranking"
    "keyword chart"
    "keyphrase chart"

*/

// create "sentiment score ranking" and "number of retweet ranking"
class createModalRanking{
    constructor(index){
        this.index = index;
        this.content = "";
        this.datasource = "";
        this.polality_json = dataset["polality_json"];
        this.retweet_json = dataset["retweet_json"];
    };

    // spesify content (polality_json or retweet_json) to create each ranking
    setContent(content){
        this.content = content;
    };

    // sort object by using value to create ranking
    sortObject(object){
        let ordered_object = Object.keys(object).map((e)=>({ key: e, object: object[e] }));
        ordered_object.sort(function(a,b){
            if(a.object < b.object) return 1;
            if(a.object > b.object) return -1;
            return 0;
        });
        return ordered_object;
    };
    
    // change dataset (polality_json or retweet_json)
    changeContent(content){
        if(content == "sentiment"){
            const datasource = this.polality_json;
            const column = "sentiment_score";
            return [datasource, column];
        }else if(content == "retweet"){
            const datasource = this.retweet_json;
            const column = "num_retweet";
            return [datasource, column];
        }else{
            console.log("invalid content");
        };
    };

    createRanking(){
        // set dataset
        const [datasource, column] = this.changeContent(this.content);

        // get data at clicked index
        const label = myLineChart.data.labels[this.index];
        const data = datasource[this.index];

        // grab html tag 
        const modal_title =  document.querySelector('.modal-title');

        const icon_1 =  document.querySelector(`.${this.content}_icon_1`);
        const icon_2 =  document.querySelector(`.${this.content}_icon_2`);
        const icon_3 =  document.querySelector(`.${this.content}_icon_3`);

        const username_1 =  document.querySelector(`.${this.content}_username_1`);
        const username_2 =  document.querySelector(`.${this.content}_username_2`);
        const username_3 =  document.querySelector(`.${this.content}_username_3`);

        const score_1 =  document.querySelector(`.${this.content}_score_1`);
        const score_2 =  document.querySelector(`.${this.content}_score_2`);
        const score_3 =  document.querySelector(`.${this.content}_score_3`);

        const text_1 =  document.querySelector(`.${this.content}_text_1`);
        const text_2 =  document.querySelector(`.${this.content}_text_2`);
        const text_3 =  document.querySelector(`.${this.content}_text_3`);

        // sort object
        const ordered_object = this.sortObject(data[column]);

        // set html value
        modal_title.innerText = label;

        const no_img_icon = "../static/twitter_analysis/img/no-image-icon.PNG"
        fetch(data["profile_img"][ordered_object[0].key])
        .then((response) => {
            if(response.ok) { 
                icon_1.setAttribute('src', data["profile_img"][ordered_object[0].key]);
            } else {
                icon_1.setAttribute('src', no_img_icon);
            }
        })
        fetch(data["profile_img"][ordered_object[1].key])
        .then((response) => {
            if(response.ok) { 
                icon_2.setAttribute('src', data["profile_img"][ordered_object[1].key]);
            } else {
                icon_2.setAttribute('src', no_img_icon);
            }
        })
        fetch(data["profile_img"][ordered_object[2].key])
        .then((response) => {
            if(response.ok) { 
                icon_3.setAttribute('src', data["profile_img"][ordered_object[2].key]);
            } else {
                icon_3.setAttribute('src', no_img_icon);
            }
        })

        username_1.innerText = data["user_screen_name"][ordered_object[0].key];
        username_2.innerText = data["user_screen_name"][ordered_object[1].key];
        username_3.innerText = data["user_screen_name"][ordered_object[2].key];

        score_1.innerText = Math.round(data[column][ordered_object[0].key] * 100) / 100; // score(rounded)
        score_2.innerText = Math.round(data[column][ordered_object[1].key] * 100) / 100; // score(rounded)
        score_3.innerText = Math.round(data[column][ordered_object[2].key] * 100) / 100; // score(rounded)

        text_1.innerText = data["text"][ordered_object[0].key];
        text_2.innerText = data["text"][ordered_object[1].key];
        text_3.innerText = data["text"][ordered_object[2].key];
    };
};

// create "keyword chart" and "keyphrase chart"
class createModalChart{
    constructor(index){
        this.index = index;
        this.content = "";
        this.keys = "";
        this.values = "";
        this.context = ""
    };

    // spesify content (keyword or kephrase) to create each chart
    setContent(content){
        this.content = content;
    };

    // get key and value from object
    setVariable(){
        const chart_dataset = dataset[`${this.content}_count`];
        const data_object = JSON.parse(chart_dataset[this.index]);
        
        this.keys = Object.keys(data_object["count"]);
        this.values = Object.values(data_object["count"]);
    
        this.context = document.getElementById(`${this.content}barChart`);
    }

    // create chart with chart.js
    createKeyWordChart(){
        // destroy existing chart first for more than second show
        if(document.keywordchart != null){
            document.keywordchart.destroy()
        };

        document.keywordchart  = new Chart(this.context, {
            type: 'bar',
            data: {
                labels: this.keys,
                datasets: [{
                    label: 'Number of Keyword',
                    data: this.values,
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
                    y: {
                        title: {
                            display: true,
                            text: 'Keyword'
                        },
                    },
                    x: {
                        ticks: {
                            beginAtZero:true,
                            callback: function(value) {
                                if (value % 1 === 0) {return value};
                            },
                        }
                    }
                }
            }
        });
    };

    createKeyPhraseChart(){
        // destroy existing chart first for more than second show
        if(document.keyphrasechart != null){
            document.keyphrasechart.destroy()
        };

        document.keyphrasechart  = new Chart(this.context, {
            type: 'bar',
            data: {
                labels: this.keys,
                datasets: [{
                    label: 'Number of Keyphrase',
                    data: this.values,
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
                    y: {
                        title: {
                            display: true,
                            text: 'Keyphrase'
                        },
                    },
                    x: {
                        ticks: {
                            beginAtZero:true,
                            callback: function(value) {
                                if (value % 1 === 0) {return value};
                            },
                        }
                    }
                }
            }
        });
    };
};



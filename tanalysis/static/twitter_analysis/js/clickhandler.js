const polality_json = dataset["polality_json"];
const retweet_json = dataset["retweet_json"];


// sort object accoring to sentiment score
function sortObject(object){
    let ordered_object = Object.keys(object).map((e)=>({ key: e, object: object[e] }));
    ordered_object.sort(function(a,b){
        if(a.object < b.object) return 1;
        if(a.object > b.object) return -1;
        return 0;
    });
    return ordered_object;
};

// change content to show depending on keywords
function changeContent(content){
    if(content == "sentiment"){
        const datasource = polality_json;
        const column = "sentiment_score";
        return [datasource, column];
    }else if(content == "retweet"){
        const datasource = retweet_json;
        const column = "num_retweet";
        return [datasource, column];
    }else{
        console.log("invalid content");
    };
};

// called from modalcontent.js
class showExampleTweet{
    constructor(index){
        this.index = index;
        this.content = "";
        this.datasource = "";
    };

    setContent(content){
        this.content = content;
    };

    setHtml(){
        // get appropiate dataset following keywords
        const [datasource, column] = changeContent(this.content);
        // get the each data according to index of cliked data
        const label= myLineChart.data.labels[this.index];
        const data = datasource[this.index];
        const modal_title =  document.querySelector('.modal-title');

        // grab html tag for user icon for sentiment score ranking
        const icon_1 =  document.querySelector(`.${this.content}_icon_1`);
        const icon_2 =  document.querySelector(`.${this.content}_icon_2`);
        const icon_3 =  document.querySelector(`.${this.content}_icon_3`);

        // grab html tag for username for sentiment score ranking
        const username_1 =  document.querySelector(`.${this.content}_username_1`);
        const username_2 =  document.querySelector(`.${this.content}_username_2`);
        const username_3 =  document.querySelector(`.${this.content}_username_3`);

        // grab html tag for sentiment score for sentiment score ranking
        const score_1 =  document.querySelector(`.${this.content}_score_1`);
        const score_2 =  document.querySelector(`.${this.content}_score_2`);
        const score_3 =  document.querySelector(`.${this.content}_score_3`);

        // grab html tag for text for sentiment score ranking
        const text_1 =  document.querySelector(`.${this.content}_text_1`);
        const text_2 =  document.querySelector(`.${this.content}_text_2`);
        const text_3 =  document.querySelector(`.${this.content}_text_3`);

        // sort object following value
        const ordered_object = sortObject(data[column]);

        // set modal titile
        modal_title.innerText = label;

        // user icon
        icon_1.setAttribute('src', data["profile_img"][ordered_object[0].key]);
        icon_2.setAttribute('src', data["profile_img"][ordered_object[1].key]);
        icon_3.setAttribute('src', data["profile_img"][ordered_object[2].key]);

        // username
        username_1.innerText = data["user_screen_name"][ordered_object[0].key];
        username_2.innerText = data["user_screen_name"][ordered_object[1].key];
        username_3.innerText = data["user_screen_name"][ordered_object[2].key];

        // score
        score_1.innerText = data[column][ordered_object[0].key];
        score_2.innerText = data[column][ordered_object[1].key];
        score_3.innerText = data[column][ordered_object[2].key];

        // text
        text_1.innerText = data["text"][ordered_object[0].key];
        text_2.innerText = data["text"][ordered_object[1].key];
        text_3.innerText = data["text"][ordered_object[2].key];
    };
};

class showModalChart{
    constructor(index){
        this.index = index;
        this.content = "";
        this.keys = "";
        this.values = "";
        this.context = ""
    };

    setContent(content){
        this.content = content;
    };

    setVariable(){
        const chart_dataset = dataset[`${this.content}_count`];
        const data_object = JSON.parse(chart_dataset[this.index]);
        
        this.keys = Object.keys(data_object["count"]);
        this.values = Object.values(data_object["count"]);
    
        this.context = document.getElementById(`${this.content}barChart`);
    }

    createKeyWordChart(){
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



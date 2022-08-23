const data_polality_json = dataset["polality_json"]
const data_retweet_json = dataset["retweet_json"]
const data_keyword = dataset["keyword_count"]

// get the data at the point of click
function getIndex(click){
    const points = myLineChart.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true);
    if (points[0]){
        const index = points[0].index;
        const content = "retweet";
        let createmodalcontent = new createModalcontent(index, content);
        console.log(createmodalcontent)
        createmodalcontent.getHtmltag();
    }
}

// sort object accoring to sentiment score
function sortObject(object){
    let ordered_object = Object.keys(object).map((e)=>({ key: e, object: object[e] }));
    ordered_object.sort(function(a,b){
        if(a.object < b.object) return 1;
        if(a.object > b.object) return -1;
        return 0;
    });
    return ordered_object
}

function changeContent(content){
    if(content == "sentiment"){
        const datasource = data_polality_json
        const column = "sentiment_score"
        return [datasource, column];
    }else if(content == "retweet"){
        const datasource = data_retweet_json
        const column = "num_retweet"
        return [datasource, column];
    }else{
        console.log("invalid content")
    }
}

class createModalcontent{
    constructor(index, content){
        this.index = index
        this.content = content
        this.datasource = ""
    }

    getHtmltag(){
            console.log(this.index)
            const [datasource, column] = changeContent(this.content);
            // get the each data according to index of cliked data
            const label= myLineChart.data.labels[this.index];
            console.log(datasource)
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

            const ordered_object = sortObject(data[column])

            // set modal titile
            modal_title.innerText = label;

            // user icon for sentiment score ranking
            icon_1.setAttribute('src', data["profile_img"][ordered_object[0].key]);
            icon_2.setAttribute('src', data["profile_img"][ordered_object[1].key]);
            icon_3.setAttribute('src', data["profile_img"][ordered_object[2].key]);

            // username for sentiment score ranking
            username_1.innerText = data["user_screen_name"][ordered_object[0].key];
            username_2.innerText = data["user_screen_name"][ordered_object[1].key];
            username_3.innerText = data["user_screen_name"][ordered_object[2].key];

            // sentiment score for sentiment score ranking
            score_1.innerText = data[column][ordered_object[0].key];
            score_2.innerText = data[column][ordered_object[1].key];
            score_3.innerText = data[column][ordered_object[2].key];

            // text for sentiment score ranking
            text_1.innerText = data["text"][ordered_object[0].key];
            text_2.innerText = data["text"][ordered_object[1].key];
            text_3.innerText = data["text"][ordered_object[2].key];
            
            // turn on modal
            let myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {});
            myModal.show();
        
    }
}
// myLineChart.canvas.onclick = clickHandler;
myLineChart.canvas.onclick = getIndex;

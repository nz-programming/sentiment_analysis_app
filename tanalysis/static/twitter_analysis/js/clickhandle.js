const data_polality_json = dataset["polality_json"]
const data_keyword = dataset["keyword_count"]

function clickHandler(click){
    // get the data at the point of click
    const points = myLineChart.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true);
    if (points[0]){
        const index = points[0].index;

        // get the each data according to index of cliked data
        const label= myLineChart.data.labels[index];
        const keyword = data_keyword[index]
        const polality_json = data_polality_json[index]
        const modal_title =  document.querySelector('.modal-title');

        // grab html tag for user icon for sentiment score ranking
        const sent_icon_1 =  document.querySelector('.sent_icon_1');
        const sent_icon_2 =  document.querySelector('.sent_icon_2');
        const sent_icon_3 =  document.querySelector('.sent_icon_3');

        // grab html tag for username for sentiment score ranking
        const sent_username_1 =  document.querySelector('.sent_username_1');
        const sent_username_2 =  document.querySelector('.sent_username_2');
        const sent_username_3 =  document.querySelector('.sent_username_3');

        // grab html tag for sentiment score for sentiment score ranking
        const sent_score_1 =  document.querySelector('.sent_score_1');
        const sent_score_2 =  document.querySelector('.sent_score_2');
        const sent_score_3 =  document.querySelector('.sent_score_3');

        // grab html tag for text for sentiment score ranking
        const sent_text_1 =  document.querySelector('.sent_text_1');
        const sent_text_2 =  document.querySelector('.sent_text_2');
        const sent_text_3 =  document.querySelector('.sent_text_3');

        // sort object accoring to sentiment score
        const sentiment_score = polality_json["sentiment_score"]    
        let arr = Object.keys(sentiment_score).map((e)=>({ key: e, value: sentiment_score[e] }));
        arr.sort(function(a,b){
            if(a.value < b.value) return 1;
            if(a.value > b.value) return -1;
            return 0;
        });

        // set modal titile
        modal_title.innerText = label;

        // user icon for sentiment score ranking
        sent_icon_1.setAttribute('src', polality_json["profile_img"][arr[0].key]);
        sent_icon_2.setAttribute('src', polality_json["profile_img"][arr[1].key]);
        sent_icon_3.setAttribute('src', polality_json["profile_img"][arr[2].key]);

        // username for sentiment score ranking
        sent_username_1.innerText = polality_json["user_screen_name"][arr[0].key];
        sent_username_2.innerText = polality_json["user_screen_name"][arr[1].key];
        sent_username_3.innerText = polality_json["user_screen_name"][arr[2].key];

        // sentiment score for sentiment score ranking
        sent_score_1.innerText = polality_json["sentiment_score"][arr[0].key];
        sent_score_2.innerText = polality_json["sentiment_score"][arr[1].key];
        sent_score_3.innerText = polality_json["sentiment_score"][arr[2].key];

        // text for sentiment score ranking
        sent_text_1.innerText = polality_json["text"][arr[0].key];
        sent_text_2.innerText = polality_json["text"][arr[1].key];
        sent_text_3.innerText = polality_json["text"][arr[2].key];
        
        // turn on modal
        let myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {});
        myModal.show();
    }
}
myLineChart.canvas.onclick = clickHandler;
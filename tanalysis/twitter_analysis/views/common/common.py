import json
from ...config.config import *

def create_dataset(queryset):
    template_name = TEMPLATE_NAME_INDEXHTML
    create_date = []
    average_polality = []
    polality_joson = []
    retweet_json = []
    keyword_count = []
    keyphrase_count = []

    queryset = queryset
    for record in queryset:
        #create date
        create_date.append(record.date)
        #sentiment score
        average_polality.append(record.average_polality)
        #JSON for sentiment score ranking
        polality_joson.append(record.polality_joson)
        #JSON for number of retweet ranking
        retweet_json.append(record.retweet_json)
        #JSON for number of keyword ranking
        keyword_count.append(record.keyword_count)
        #JSON for number of keyphrase ranking
        keyphrase_count.append(record.keyphrase_count)
        
    var = {
        'create_date': create_date,
        'average_polality': average_polality,
        'polality_json':polality_joson,
        'retweet_json':retweet_json,
        'keyword_count':keyword_count,
        'keyword_count':keyphrase_count
    }
    
    dataset = {'data_json':json.dumps(var, default=str)}
    return (template_name, dataset)
from subprocess import CREATE_DEFAULT_ERROR_MODE
import datetime

TEMPLATE_NAME_INDEXHTML = 'twitter_analysis/index.html'

TODAY = datetime.date.today()
SHOW_PERIOD_WEEK = datetime.timedelta(7)
SHOW_PERIOD_MONTH = datetime.timedelta(30)
SHOW_PERIOD_YEAR = datetime.timedelta(364)


# urls.py
PATH_INDEX = "index"
PATH_WEEKBUTTON = "week"
PATH_MONTHBUTTON = "month"
PATH_YEARBUTTON = "year"


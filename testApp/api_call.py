import requests
from bs4 import BeautifulSoup as Bs
import json
import re
import pandas as pd
import datetime


def get_last_page_no(mk, md, ct):
    link = "https://www.pakwheels.com/used-cars/search/-/ct_" + ct + "/mk_" + mk + "/md_" + md + "/?page=1000&sortby=model_year-asc"
    fetch = requests.get(link, allow_redirects=True)
    page = fetch.text
    html = Bs(page, 'html.parser')
    try:
        no_elem = html.find("div", class_='well suggestions-noresults search-main').text
    except AttributeError:
        no_elem = None
    element = html.findAll("li", class_='page')
    if no_elem is not None:
        return None
    if len(element) == 0:
        final_dest = 1
    else:
        final_dest = element[len(element) - 1].text
    return int(final_dest)


def is_updated(update):
    updated = False
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
              'Nov': 11, 'Dec': 12}
    year = int(update[-4:])
    month = update[3: 6]
    month = months[month]
    # date = int(update[:2])
    cur_month = datetime.datetime.now().month
    cur_year = datetime.datetime.now().year
    if year == cur_year:
        if month == cur_month or month == cur_month - 1:
            updated = True
    return updated


def get_pages_data(u):
    d = []
    for url in u:
        try:
            response = requests.get(url)

            b = Bs(response.text, 'html.parser')
            add_ids = re.findall('main_ad_[0-9]+', response.text)
            lis = [b.find('li', id=i) for i in add_ids]
            objs = []
            for id_ in lis:
                try:
                    objs.append(id_.find('script').text.strip().replace("\n", "").replace("  ", ""))
                except:
                    pass
            js = [json.loads(obj) for obj in objs]
            for jp in js:
                d.append([jp['modelDate'], jp['offers']['price']])
        except:
            pass
    return d


def get_data_pw(make, model, city):

    last_page = get_last_page_no(make, model, city)
    if last_page is None:
        return None
    if last_page > 1:
        urls = ["https://www.pakwheels.com/used-cars/search/-/ct_" + city + "/mk_" + make + "/md_" + model + "/?page=" + str(j) for j in range(1, 20)]

    else:
        urls = ["https://www.pakwheels.com/used-cars/search/-/ct_" + city + "/mk_" + make + "/md_" + model + "/?page=1"]

    data = get_pages_data(urls)
    df = pd.DataFrame(data, columns=['year', 'price'])
    return df


def millify(num):
    number = str(num)
    if len(number) == 7:
        milli = number[0] + "." + number[1:3] + "M"
    elif len(number) == 6:
        milli = "0." + number[0:2] + "M"
    elif len(number) == 5:
        milli = number[:2] + "K"
    elif len(number) == 8:
        milli = number[:2] + "M"
    else:
        milli = num
    return milli

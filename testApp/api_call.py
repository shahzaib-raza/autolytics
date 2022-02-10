import requests
from bs4 import BeautifulSoup as Bs
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
        response = requests.get(url)
        obj = response.json()['result']
        for i in range(len(obj)):
            price = obj[i]['price']
            update = obj[i]['last_updated']
            if is_updated(update) is False and price == "Call for Price":
                pass
            else:
                try:
                    year = obj[i]['model_year']
                    d.append([int(year), int(price)])
                except ValueError:
                    pass
    return d


def get_data_pw(make, model, city):

    last_page = get_last_page_no(make, model, city)
    if last_page is None:
        return None
    if last_page > 1:
        urls = ["https://www.pakwheels.com/used-cars/search/-/ct_" + city + "/mk_" + make + "/md_" + model + ".json?client_id=37952d7752aae22726aff51be531cddd&client_secret=014a5bc91e1c0f3af4ea6dfaa7eee413&api_version=15&sortby=model_year-asc&page=" + str(j) + "&extra_info=true" for j in range(1, 20)]

    else:
        urls = ["https://www.pakwheels.com/used-cars/search/-/ct_" + city + "/mk_" + make + "/md_" + model + ".json?client_id=37952d7752aae22726aff51be531cddd&client_secret=014a5bc91e1c0f3af4ea6dfaa7eee413&api_version=15&sortby=model_year-asc&page=1&extra_info=true"]

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

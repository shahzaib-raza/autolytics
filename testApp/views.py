from django.shortcuts import render
from plotly.offline import plot
from .api_call import get_data_pw, millify

from plotly import subplots
import plotly.graph_objs as go


# Create your views here.
def appView(request, mm, mn, ct):
    mm = mm.strip()
    mn = mn.strip()
    ct = ct.strip()
    data = get_data_pw(mm, mn, ct)
    if data is None:
        return render(request, "sorry.html")
    mm = mm.capitalize()
    mn = mn.capitalize()
    ct = ct.capitalize()
    tit = mm + " " + mn + " (" + ct + ")"
    fory = data['year'].value_counts()[:]
    forx = data['year'].value_counts().index.tolist()
    sp = subplots.make_subplots(rows=2, cols=1, subplot_titles=['Price_Scatter', 'Quantity_Bars'])
    sp.add_trace(go.Scatter(x=data['year'],
                            y=data['price'],
                            mode='markers',
                            marker={'color': 'tomato', 'size': 12},
                            ), row=1, col=1)
    sp.add_trace(go.Bar(x=forx, y=fory), row=2, col=1)

    sp.update_layout({
        'plot_bgcolor': 'rgba(79, 83, 88, 0)',
        'paper_bgcolor': 'rgba(79, 83, 88, 0.4)',
        'font_color': 'rgba(255, 255, 255, 1)',
        'font_size': 15,
        'autosize': True,
        'height': 800,
        'title': tit
    })
    plot_div = plot({'data': sp}, output_type='div')
    min_price = int(min(data['price']))
    avg_price = int(sum(data['price']) / len(data['price']))
    max_price = int(max(data['price']))
    mini = millify(min_price)
    price = millify(avg_price)
    maxi = millify(max_price)
    return render(request, "index.html", context={
        "plot_div": plot_div,
        "avg_price": price,
        "min_price": mini,
        "max_price": maxi,
    })


def model_name(request):
    if request.method == 'GET':
        make = request.GET.get('make')
        model = request.GET.get('model')
        city = request.GET.get('city')
        if make is not None and model is not None and city is not None:
            return appView(request, make, model, city)

    return render(request, 'results.html')

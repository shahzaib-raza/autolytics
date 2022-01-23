from django.shortcuts import render
from plotly.offline import plot
from .forms import InputForm
from .api_call import get_data_pw, millify

from plotly import subplots
import plotly.graph_objs as go


# Create your views here.
def appView(request, mm, mn, ct):
    mm = mm.strip()
    mn = mn.strip()
    ct = ct.strip()
    data = get_data_pw(mm, mn, ct)
    mm = mm.capitalize()
    mn = mn.capitalize()
    ct = ct.capitalize()
    print(f"Input make is: {mm}")
    print(f"Input model is: {mn}")
    print(f"Input city is: {ct}")
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
        form = InputForm(request.GET)
        vals = form.data.dict()
        make = vals.get("make")
        make = str(make).lower()
        model = vals.get("model")
        model = str(model).lower()
        city = vals.get("city")
        city = str(city).lower()
        if form.is_valid():
            return appView(request, make, model, city)
    else:
        form = InputForm()
    return render(request, 'results.html', {'form': form})

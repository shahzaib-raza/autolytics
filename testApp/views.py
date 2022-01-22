from django.shortcuts import render
import plotly.express as px
from plotly.offline import plot
from .forms import InputForm
from .api_call import get_data_pw, millify


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
    fig = px.scatter(x=data['year'],
                     y=data['price'],
                     title=tit, labels={"x": "Model years", "y": "Prices"},
                     trendline='ols',
                     trendline_options=dict(log_y=True),
                     trendline_color_override='red')
    fig.update_layout({
        'plot_bgcolor': 'rgba(79, 83, 88, 0)',
        'paper_bgcolor': 'rgba(79, 83, 88, 0.4)',
        'font_color': 'rgba(255, 255, 255, 1)',
        'font_size': 10,
        'autosize': True,
    })
    fory = data['year'].value_counts()[:]
    forx = data['year'].value_counts().index.tolist()
    fig1 = px.bar(x=forx, y=fory, labels={"x": "Model years", "y": "Frequency"})
    fig1.update_layout({
        'plot_bgcolor': 'rgba(79, 83, 88, 0)',
        'paper_bgcolor': 'rgba(79, 83, 88, 0.4)',
        'font_color': 'rgba(255, 255, 255, 1)',
        'font_size': 10,
        'autosize': True,
    })
    plot_div = plot({'data': fig}, output_type='div')
    plot_div1 = plot({'data': fig1}, output_type='div')
    min_price = int(min(data['price']))
    avg_price = int(sum(data['price'])/len(data['price']))
    max_price = int(max(data['price']))
    mini = millify(min_price)
    price = millify(avg_price)
    maxi = millify(max_price)
    return render(request, "index.html", context={
        "plot_div": plot_div,
        "plot_div1": plot_div1,
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

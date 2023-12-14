from django.shortcuts import render
from plotly.offline import plot
from .api_call import get_data_pw, millify
import pandas as pd
from plotly import subplots
import plotly.graph_objs as go


def get_int(x):
    try:
        return float(x)
    except:
        return None

# Create your views here.
def appView(request, mm, mn, ct):
    data = get_data_pw(mm, mn, ct)
    if data is None:
        return render(request, "sorry.html")
    data['price'].apply(get_int)
    data['year'].apply(get_int)
    mm = mm.strip().capitalize()
    mn = mn.strip().capitalize()
    ct = ct.strip().capitalize()
    tit = mm + " " + mn + " (" + ct + ")"

    # Formatting data for bar plot
    fory = data['year'].value_counts()[:]
    
    sp = subplots.make_subplots(
                rows=3,
                cols=1,
                subplot_titles=['Price_Scatter', 'Quantity_Bars', 'Detail Bars'],
                specs=[[{"type": "xy"}],
                       [{"type": "xy"}],
                       [{"type": "polar"}]]
            )
    
    sp.add_trace(go.Scatter(x=data['year'],
                            y=data['price'],
                            name="Each Available "+mn+" Price",
                            mode='markers',
                            marker={'color': 'tomato', 'size': 12},
                            hovertemplate="<br>".join([
                                "year: %{x}",
                                "price: "+"%{y}",
                            ]),
                            hoverlabel={'font': {'color': 'white'}}
                        ),
                    row=1,
                    col=1
                )
    
    sp.add_trace(go.Bar(x=fory.index.tolist(),
                        y=fory,
                        name="No. of "+mn+" for sale per year",
                        hovertemplate="<br>".join([
                                "year: %{x}",
                                f"No. of {mn} found: "+"%{y}",
                            ]),
                            hoverlabel={'font': {'color': 'white'}}
                       ),
                    row=2,
                    col=1
                )

    # Formatting data for C_bar 
    grouped_data = data.groupby(['year'])
    gd_min_price = grouped_data.min().reset_index()['price'].tolist()
    gd_max_price = grouped_data.max().reset_index()['price'].tolist()
    gd_years = grouped_data.mean().reset_index()['year'].tolist()
    gd_mean_price = grouped_data.mean().reset_index()['price'].round(2).tolist()

    sp.add_trace(
            go.Barpolar(r=gd_min_price,
                        name='Min Price Per Year',
                        marker_color='rgb(255, 170, 51)',
                        text=gd_years,
                        hovertemplate="<br>".join([
                                "year: %{text}",
                                "min_price: %{r}",
                            ]),
                        hoverlabel={'font': {'color': 'white'}}
                       ),
            row=3,
            col=1,
        )
    
    sp.add_trace(
            go.Barpolar(r=gd_mean_price,
                        name='Mean Price Per Year',
                        marker_color='rgb(236, 88, 0)',
                        text=gd_years,
                        hovertemplate="<br>".join([
                                "year: %{text}",
                                "mean_price: %{r}",
                            ]),
                        hoverlabel={'font': {'color': 'white'}}
                       ),
            row=3,
            col=1,
    )

    sp.add_trace(
            go.Barpolar(r=gd_max_price,
                        marker_color='rgb(139, 64, 0)',
                        name='Max Price Per Year',
                        text=gd_years,
                        hovertemplate="<br>".join([
                                "year: %{text}",
                                "max_price: %{r}",
                            ]),
                        hoverlabel={'font': {'color': 'white'}}
                       ),
            row=3,
            col=1,
    )

    sp.update_layout({
        'plot_bgcolor': 'rgba(79, 83, 88, 0)',
        'paper_bgcolor': 'rgba(79, 83, 88, 0.4)',
        'font_color': 'rgba(255, 255, 255, 1)',
        'font_size': 15,
        'autosize': True,
        'height': 1800,
        'title': tit,
        'polar_bgcolor': 'rgba(79, 83, 88, 0.4)',
        'polar_angularaxis_visible': False,
        'polar_angularaxis_showticklabels': True,
        'polar_angularaxis_ticks': "",
        'polar_radialaxis_ticks': None,
        'polar_radialaxis_visible': False,
        'polar_radialaxis_showticklabels': False,
    })
    
    prc = data[data['price'].notna()]['price']
    plot_div = plot({'data': sp}, output_type='div')
    min_price = int(prc.min())
    avg_price = int(prc.sum() / len(prc))
    max_price = int(prc.max())
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

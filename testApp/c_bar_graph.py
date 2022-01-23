import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def c_bar_plot(data):
    df_c = data.groupby(['year']).mean().reset_index()
    fyear = df_c['year'].tolist()
    tprice = df_c['price'].tolist()
    rtprice=['%.2f' % elem for elem in tprice ]
    groups=[]
    for i in range(len(fyear)):
        groups.append(str(fyear[i])+" : " + str(rtprice[i]))
    df = pd.DataFrame({
        "name": fyear,
        "value": tprice,
        "group": groups
    })
    # set figure size
    plt.figure(figsize=(20,10))
    # plot polar axis
    ax = plt.subplot(111, polar=True)
    # remove grid
    plt.axis('off')
    # Set the coordinates limits
    upperLimit = 100
    lowerLimit = 30
    # Compute max and min in the dataset
    max = df['value'].max()
    # Let's compute heights: they are a conversion of each item value in those new coordinates
    # In our example, 0 in the dataset will be converted to the lowerLimit (10)
    # The maximum will be converted to the upperLimit (100)
    slope = (max - lowerLimit) / max
    heights = slope * df.value + lowerLimit
    # Compute the width of each bar. In total we have 2*Pi = 360°
    width = 2*np.pi / len(df.index)
    # Compute the angle each bar is centered on:
    indexes = list(range(1, len(df.index)+1))
    angles = [element * width for element in indexes]

    # Draw bars
    bars = ax.bar(
        x=angles,
        height=heights,
        width=width,
        bottom=lowerLimit,
        linewidth=2,
        edgecolor="white",
        color="#61a4b2",
    )

    # little space between the bar and the label
    labelPadding = 4
    # Add labels
    for bar, angle, height, label in zip(bars,angles, heights, df["group"]):

        # Labels are rotated. Rotation must be specified in degrees :(
        rotation = np.rad2deg(angle)

        # Flip some labels upside down
        alignment = ""
        if np.pi/2 <= angle < 3*np.pi/2:
            alignment = "right"
            rotation = rotation + 180
        else:
            alignment = "left"

        # Finally add the labels
        ax.text(
            x=angle,
            y=lowerLimit + bar.get_height() + labelPadding,
            s=label,
            ha=alignment,
            va='center',
            rotation=rotation,
            rotation_mode="anchor")


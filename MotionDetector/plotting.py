from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["start_string"]=df["start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["end_string"]=df["end"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type="datetime", height=100, width=500, sizing_mode="stretch_both", title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.yaxis[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start", "@start_string"), ("End", "@end_string")])
p.add_tools(hover)

q=p.quad(left="start", right="end", bottom=0, top=1, color="green", source=cds)

output_file("Graph1.html")
show(p)

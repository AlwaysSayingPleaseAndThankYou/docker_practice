import numpy as np
import pandas as pd
import panel as pn

df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD')).cumsum()

rollover = pn.widgets.IntInput(name='Rollover', value=15)

perspective = pn.pane.Perspective(
    df, sizing_mode='stretch_width', height=400, theme='material-dark'
)

def stream():
    data = df.iloc[-1] + np.random.randn(4)
    perspective.stream(data, rollover=rollover.value)

cb = pn.state.add_periodic_callback(stream, 50)

component = pn.Column(
    pn.Row(cb.param.period, rollover, perspective.param.theme),
    perspective,
    pn.layout.HSpacer(height=35), # Needed if user selects vaporwave theme in template
)
pn.serve(panels=component,
         port=8000,
         show=True,
         title='foobar',
         websocket_origin=['localhost:8000'])

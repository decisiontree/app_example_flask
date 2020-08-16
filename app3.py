from flask import Flask, render_template, request
import json
from plotly.utils import PlotlyJSONEncoder
import numpy as np
from pandas import read_csv
import plotly.express as px

#http://localhost:5000/graph?bins=3

faithful = read_csv('./data/faithful.csv')
app = Flask(__name__)

@app.route('/graph')
def hist():
  bins = int(request.args['bins'])
  x = faithful['waiting']
  counts, bins = np.histogram(x, bins=np.linspace(np.min(x), np.max(x), bins+1))
  bins = 0.5* (bins[:-1] + bins[1:])
  p = px.bar(
    x=bins, y=counts,
    title='Histogram of waiting times',
    labels={
      'x': 'Waiting time to next eruption (in mins)',
      'y': 'Frequency'
    },
    template='simple_white'
  )
  return json.dumps(p, cls=PlotlyJSONEncoder)


# At the end of our script
if __name__ == '__main__':
  app.run()





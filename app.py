from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Sample data
names = ["Name 1", "Name 2", "Name 3","Name 4"]
dataframes = [
    pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6],"C":[2,4,""]}),
    pd.DataFrame({"X": [7, 8, 9], "Y": [10, 11, 12]}),
    pd.DataFrame({"P": [13, 14, 15], "Q": [16, 17, 18]}),
    pd.DataFrame({"Z": [13, 14, 15], "Q": [16, 17, 18]})
]
for df in dataframes:
    df.reset_index(drop=True, inplace=True)
length = len(names)

@app.route('/')
def index():
    return render_template('index.html', names=names, dataframes=dataframes, length=length)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    dict1 = {
        "hello": {
            "High": ["Item1", "Item2","Item11", "Item21","Item12", "Item22","Item13", "Item23","Item14", "Item24","Item15", "Item25"],
            "Low": ["Item3", "Item4", "Item5"],
            "Normal": ["Item6", "Item7", "Item8"]
        },
        "man": {
            "High": ["Item1", "Item2"],
            "Low": ["Item3"],
            "Normal": ["Item4", "Item5"]
        }
    }

    # Create a list of dataframes and counts for pie charts
    dataframes = {}
    pie_data = {}
    for key, value in dict1.items():
        rows = []
        counts = {'High': 0, 'Low': 0, 'Normal': 0}
        for impact, items in value.items():
            counts[impact] += len(items)
            for item in items:
                color_class = 'high' if impact == 'High' else 'low' if impact == 'Low' else 'normal'
                rows.append({'Impact': impact, 'Item': item, 'ColorClass': color_class})
        df = pd.DataFrame(rows)
        dataframes[key] = df
        pie_data[key] = counts

    return render_template('index.html', dataframes=dataframes, pie_data=pie_data)

if __name__ == '__main__':
    app.run(debug=True)


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expandable Cards with DataTables</title>
    <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .high { background-color: red; }
        .normal { background-color: orange; }
        .low { background-color: yellow; }
        .chart-container {
            position: relative;
            width: 100%;
            height: 400px; /* default height */
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        {% for key, df in dataframes.items() %}
        <div class="card mb-3">
            <div class="card-header">
                <h5 class="mb-0">
                    <button class="btn btn-link" data-bs-toggle="collapse" data-bs-target="#collapse{{ loop.index }}" aria-expanded="true" aria-controls="collapse{{ loop.index }}">
                        {{ key }}
                    </button>
                </h5>
            </div>
            <div id="collapse{{ loop.index }}" class="collapse" data-bs-parent="#accordion">
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-8">
                            <table class="table table-striped dataTable" id="dataTable{{ loop.index }}">
                                <thead>
                                    <tr>
                                        <th>Impact</th>
                                        <th>Item</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for row in df.itertuples() %}
                                    <tr class="{{ row.ColorClass }}">
                                        <td>{{ row.Impact }}</td>
                                        <td>{{ row.Item }}</td>
                                    </tr>
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                        <div class="col-md-4">
                            <div class="chart-container">
                                <canvas id="pieChart{{ loop.index }}"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>

    <script>
        $(document).ready(function() {
            {% for key, counts in pie_data.items() %}
            var ctx = document.getElementById('pieChart{{ loop.index }}').getContext('2d');
            var pieChart = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: ['High', 'Low', 'Normal'],
                    datasets: [{
                        data: [{{ counts['High'] }}, {{ counts['Low'] }}, {{ counts['Normal'] }}],
                        backgroundColor: ['red', 'yellow', 'orange']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            var dataTable = $('#dataTable{{ loop.index }}').DataTable({
                "pageLength": 5,
                "drawCallback": function(settings) {
                    adjustChartContainerHeight('{{ loop.index }}');
                }
            });

            // Adjust chart container height based on DataTable
            function adjustChartContainerHeight(index) {
                var tableHeight = $('#dataTable' + index + '_wrapper .dataTables_scrollBody').height();
                $('#collapse' + index + ' .chart-container').css('height', tableHeight);
            }

            adjustChartContainerHeight('{{ loop.index }}');

            {% endfor %}
        });
    </script>
</body>
</html>

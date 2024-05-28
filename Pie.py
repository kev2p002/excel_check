from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data_sets = [
        [{'label': 'High', 'value': 20}, {'label': 'Low', 'value': 15}, {'label': 'Medium', 'value': 20}],
        [{'label': 'High', 'value': 25}, {'label': 'Low', 'value': 10}, {'label': 'Medium', 'value': 30}],
        # Add more data sets if needed
    ]
    return render_template('index.html', data_sets=data_sets)

if __name__ == '__main__':
    app.run(debug=True)


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pie Charts</title>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Pie Charts</h1>
        <div class="row">
            {% for i, data in enumerate(data_sets) %}
            <div class="col-md-6 mb-4">
                <canvas id="myPieChart{{ i }}"></canvas>
            </div>
            {% endfor %}
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const dataSets = {{ data_sets|tojson }};
            dataSets.forEach((data, index) => {
                const labels = data.map(item => item.label);
                const values = data.map(item => item.value);

                const ctx = document.getElementById('myPieChart' + index).getContext('2d');
                new Chart(ctx, {
                    type: 'pie',
                    data: {
                        labels: labels,
                        datasets: [{
                            data: values,
                            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'],
                        }]
                    },
                    options: {
                        responsive: true,
                        legend: {
                            position: 'top',
                        },
                        title: {
                            display: true,
                            text: `Pie Chart ${index + 1}`
                        }
                    }
                });
            });
        });
    </script>
</body>
</html>

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
    <style>
        .chart-canvas {
            width: 100% !important;
            height: 400px !important;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Pie Charts</h1>
        <div class="accordion" id="accordionExample">
            {% for i in range(data_sets|length) %}
            <div class="card">
                <div class="card-header" id="heading{{ i }}">
                    <h2 class="mb-0">
                        <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{{ i }}" aria-expanded="true" aria-controls="collapse{{ i }}">
                            Pie Chart {{ i + 1 }}
                        </button>
                    </h2>
                </div>

                <div id="collapse{{ i }}" class="collapse {% if i == 0 %}show{% endif %}" aria-labelledby="heading{{ i }}" data-parent="#accordionExample">
                    <div class="card-body">
                        <canvas id="myPieChart{{ i }}" class="chart-canvas"></canvas>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const dataSets = {{ data_sets|tojson }};
            const charts = [];

            dataSets.forEach((data, index) => {
                const labels = data.map(item => item.label);
                const values = data.map(item => item.value);

                const ctx = document.getElementById('myPieChart' + index).getContext('2d');
                const chart = new Chart(ctx, {
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
                        plugins: {
                            legend: {
                                position: 'top',
                            },
                            title: {
                                display: true,
                                text: `Pie Chart ${index + 1}`
                            }
                        }
                    }
                });

                charts.push(chart);
            });

            // Re-draw charts when the collapse event occurs
            $('.collapse').on('shown.bs.collapse', function () {
                const canvasId = $(this).find('canvas').attr('id');
                const index = canvasId.replace('myPieChart', '');
                charts[index].resize();
            });
        });
    </script>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

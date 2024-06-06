<script>
    $(document).ready(function() {
        var dataTables = {};
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
        dataTables['dataTable{{ loop.index }}'] = dataTable;

        // Adjust chart container height based on DataTable
        function adjustChartContainerHeight(index) {
            var tableHeight = $('#dataTable' + index + '_wrapper .dataTables_scrollBody').height();
            $('#collapse' + index + ' .chart-container').css('height', tableHeight);
        }

        adjustChartContainerHeight('{{ loop.index }}');

        {% endfor %}

        // Add event listener for interaction dropdown
        $(document).on('change', '.interaction-dropdown', function() {
            var row = $(this).closest('tr');
            if ($(this).val() === 'No Interaction') {
                row.addClass('strikeout');
                row.find('.rationale-input').removeClass('strikeout');
            } else {
                row.removeClass('strikeout');
            }
        });

        // Add event listener for the download all button
        $('#downloadAllBtn').on('click', function() {
            var title = $('#titleInput').val().trim();
            if (!title) {
                alert('Please enter a title.');
                return;
            }

            var sheets = [];
            {% for key in dataframes.keys() %}
            var dataTable = dataTables['dataTable{{ loop.index }}'];
            var rows = [];
            dataTable.rows().every(function() {
                var row = $(this.node());
                var impact = row.find('td').eq(0).text();
                var item = row.find('td').eq(1).text();
                var interaction = row.find('select').val();
                var rationale = row.find('input.rationale-input').val();
                rows.push({ 'Impact': impact, 'Item': item, 'Interaction': interaction, 'Rationale': rationale });
            });
            sheets.push({ key: '{{ key }}', rows: rows });
            {% endfor %}

            // Send data to Flask endpoint to generate Excel file
            $.ajax({
                url: '/download_excel',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ title: title, sheets: sheets }),
                xhrFields: {
                    responseType: 'blob'
                },
                success: function(blob) {
                    var url = window.URL.createObjectURL(blob);
                    var a = document.createElement('a');
                    a.style.display = 'none';
                    a.href = url;
                    a.download = 'all_data.xlsx';
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                },
                error: function() {
                    alert('Error downloading file.');
                }
            });
        });
    });
</script>


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
        .dataTables_wrapper .dataTables_filter {
            margin-bottom: 15px; /* space between search bar and table */
        }
        .dataTables_wrapper .dataTables_paginate {
            margin-top: 15px; /* space between table and pagination */
        }
        .strikeout td {
            text-decoration: line-through;
        }
        .strikeout input.rationale-input {
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <div class="form-group">
            <label for="titleInput">Title</label>
            <input type="text" class="form-control" id="titleInput" placeholder="Enter title">
        </div>
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
                                        <th>Interaction</th>
                                        <th>Rationale</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for row in df.itertuples() %}
                                    <tr class="{{ row.ColorClass }}">
                                        <td>{{ row.Impact }}</td>
                                        <td>{{ row.Item }}</td>
                                        <td>
                                            <select class="form-select interaction-dropdown" data-row="{{ loop.index }}" data-item="{{ row.Item }}">
                                                <option value="Select">Select</option>
                                                <option value="Major">Major</option>
                                                <option value="Minor">Minor</option>
                                                <option value="No Interaction">No Interaction</option>
                                            </select>
                                        </td>
                                        <td>
                                            <input type="text" class="form-control rationale-input" value="Default rationale">
                                        </td>
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
        <button class="btn btn-primary mt-3" id="downloadAllBtn">Download All Data</button>
    </div>
</body>
</html>


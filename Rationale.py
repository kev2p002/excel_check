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
        .strikeout {
            text-decoration: line-through;
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
                                            <input type="text" class="form-control rationale-input" style="background-color: black; color: white;">
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
        <div class="mt-3">
            <input type="text" class="form-control d-inline" id="titleInput" placeholder="Enter title" style="width: 300px; margin-right: 10px;">
            <button class="btn btn-primary d-inline" id="downloadAllBtn">Download All Data</button>
        </div>
    </div>
</body>
</html>



@app.route('/download_excel', methods=['POST'])
def download_excel():
    data = request.json
    title = data.get('title', 'Data')
    sheets_data = data['sheets']

    output = io.BytesIO()
    workbook = Workbook()
    workbook.remove(workbook.active)  # Remove default sheet

    for sheet_data in sheets_data:
        key = sheet_data['key']
        rows = sheet_data['rows']
        df = pd.DataFrame(rows)
        sheet = workbook.create_sheet(title=key)

        # Adding title as the first row
        title_cell = sheet.cell(row=1, column=1, value=title)
        sheet.merge_cells(start_row=1, start_column=1, end_row=1, end_column=5)
        
        # Centering the title
        title_cell.alignment = Alignment(horizontal="center", vertical="center")

        # Adding headers
        headers = ['Impact', 'Item', 'Interaction', 'Rationale', 'Alerts']
        sheet.append(headers)

        # Adding data with 'Alerts' column
        for _, row in df.iterrows():
            alert_color = 'FFFFFF'  # Default white
            if row['Impact'] == 'High':
                alert_color = 'FF0000'  # Red
            elif row['Impact'] == 'Low':
                alert_color = 'FFFF00'  # Yellow
            elif row['Impact'] == 'Normal':
                alert_color = 'FFA500'  # Orange

            alert_cell = PatternFill(start_color=alert_color, end_color=alert_color, fill_type="solid")
            new_row = [row['Impact'], row['Item'], row['Interaction'], row['Rationale'], '']
            sheet.append(new_row)

            # Set alert color for the last cell
            for cell in sheet[-1]:
                if cell.value == '':
                    cell.fill = alert_cell

    workbook.save(output)
    output.seek(0)

    return send_file(output, attachment_filename="all_data.xlsx", as_attachment=True)

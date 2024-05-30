app.py
from flask import Flask, render_template, request, flash
from forms import DocumentForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = DocumentForm()
    if form.validate_on_submit():
        docx1 = form.docx1.data
        xlsx1 = form.xlsx1.data
        docx2 = form.docx2.data
        xlsx2 = form.xlsx2.data
        docx3 = form.docx3.data
        xlsx3 = form.xlsx3.data

        filenames = []
        for file in [docx1, xlsx1, docx2, xlsx2, docx3, xlsx3]:
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filenames.append(filename)

        flash('Files successfully uploaded', 'success')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)


forms.py
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class DocumentForm(FlaskForm):
    docx1 = FileField('Document 1 (.docx)', validators=[DataRequired()])
    xlsx1 = FileField('Spreadsheet 1 (.xlsx)', validators=[DataRequired()])
    docx2 = FileField('Document 2 (.docx)', validators=[DataRequired()])
    xlsx2 = FileField('Spreadsheet 2 (.xlsx)', validators=[DataRequired()])
    docx3 = FileField('Document 3 (.docx)', validators=[DataRequired()])
    xlsx3 = FileField('Spreadsheet 3 (.xlsx)', validators=[DataRequired()])
    submit = SubmitField('Upload')

    def validate_docx1(self, field):
        if not field.data.filename.endswith('.docx'):
            raise ValidationError('File must be a .docx')

    def validate_xlsx1(self, field):
        if not field.data.filename.endswith('.xlsx'):
            raise ValidationError('File must be a .xlsx')

    def validate_docx2(self, field):
        if not field.data.filename.endswith('.docx'):
            raise ValidationError('File must be a .docx')

    def validate_xlsx2(self, field):
        if not field.data.filename.endswith('.xlsx'):
            raise ValidationError('File must be a .xlsx')

    def validate_docx3(self, field):
        if not field.data.filename.endswith('.docx'):
            raise ValidationError('File must be a .docx')

    def validate_xlsx3(self, field):
        if not field.data.filename.endswith('.xlsx'):
            raise ValidationError('File must be a .xlsx')

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Verification</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <link href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1>Document Verification</h1>
        <form method="POST" enctype="multipart/form-data">
            {{ form.hidden_tag() }}
            <div class="card mb-3">
                <div class="card-header">Group 1</div>
                <div class="card-body">
                    <div class="form-group">
                        {{ form.docx1.label }}
                        {{ form.docx1(class="form-control") }}
                    </div>
                    <div class="form-group">
                        {{ form.xlsx1.label }}
                        {{ form.xlsx1(class="form-control") }}
                    </div>
                </div>
            </div>
            <div class="card mb-3">
                <div class="card-header">Group 2</div>
                <div class="card-body">
                    <div class="form-group">
                        {{ form.docx2.label }}
                        {{ form.docx2(class="form-control") }}
                    </div>
                    <div class="form-group">
                        {{ form.xlsx2.label }}
                        {{ form.xlsx2(class="form-control") }}
                    </div>
                    <div class="form-group">
                        {{ form.docx3.label }}
                        {{ form.docx3(class="form-control") }}
                    </div>
                    <div class="form-group">
                        {{ form.xlsx3.label }}
                        {{ form.xlsx3(class="form-control") }}
                    </div>
                </div>
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="alert alert-info mt-3">
                    {% for category, message in messages %}
                        <p>{{ message }}</p>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

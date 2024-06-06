<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Input Example</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Enter Text</h1>
        <form method="post" action="/">
            <div class="form-group">
                <label for="user_input">Your Input</label>
                <input type="text" class="form-control" id="user_input" name="user_input" placeholder="Enter something...">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        print(f"User Input: {user_input}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

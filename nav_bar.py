from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)



<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap" rel="stylesheet">

    <style>
      .navbar-nav {
        width: 100%;
        justify-content: space-around;
      }
      .navbar-light {
        background-color: #f8f9fa;
      }
      .nav-link {
        color: #007bff;
        font-weight: bold;
        transition: color 0.3s;
      }
      .nav-link:hover {
        color: #0056b3;
      }
      .home-link {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        color: #ff5733 !important;
        padding: 10px 20px;
        border: 2px solid #ff5733;
        border-radius: 5px;
        background-color: #f8f9fa;
        transition: background-color 0.3s, color 0.3s, transform 0.3s;
        display: flex;
        align-items: center;
      }
      .home-link i {
        margin-right: 10px;
        transition: transform 0.3s;
      }
      .home-link:hover {
        color: #fff !important;
        background-color: #ff5733;
        transform: scale(1.1);
      }
      .home-link:hover i {
        transform: rotate(360deg);
      }
    </style>

    <title>Flask App with Stylish Home Button</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="container">
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mx-auto">
            <li class="nav-item">
              <a class="nav-link home-link" href="/">
                <i class="fas fa-home"></i> Home
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/about">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/contact">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container mt-4">
      {% block content %}{% endblock %}
    </div>

    <!-- Optional JavaScript; choose one of the two! -->
    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  </body>
</html>

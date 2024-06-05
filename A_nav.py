<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">

    <style>
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
        font-family: 'Pacifico', cursive;
        font-size: 2.5rem;
        color: #ff5733 !important;
        padding: 5px 15px;
        border-radius: 5px;
        transition: transform 0.3s, text-shadow 0.3s;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
      }
      .home-link:hover {
        transform: scale(1.1);
        text-shadow: 3px 3px 7px rgba(0,0,0,0.5);
      }
    </style>

    <title>Flask App with Stylish Home Button</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="container">
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav w-100">
            <li class="nav-item mr-auto">
              <a class="nav-link" href="/about">About</a>
            </li>
            <li class="nav-item mx-auto">
              <a class="nav-link home-link" href="/">Home</a>
            </li>
            <li class="nav-item ml-auto">
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

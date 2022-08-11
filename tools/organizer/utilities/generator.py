def html(project_name):
  content_html = f"""<!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- CSS external -->
    <link rel="stylesheet" href="assets/css/style.css">
    <title>{project_name}</title>
  </head>
  <body>
    <h1>{project_name}</h1>

    <!-- Script external -->
    <script src="assets/js/script.js"></script>
  </body>
  </html>"""
  return content_html

def css(font):
  content_css = """* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

@import url('https://fonts.googleapis.com/css2?family=%s:wght@300;400;700&display=swap');

body{
  background:#7b8d6b;
  font-family: '%s', sans-serif;
}

h1 {
  background-color: #625e5e;
  padding: 10px;
  text-align: center;
  color:azure;
}
""" % (font, font)

  return content_css

def js():
  content_js = """// Your code here
  
  """
  return content_js


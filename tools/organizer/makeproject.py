import os
from utilities.generator import html, css, js

def makeVoidProject(path: str, project_name: str):
  folders = {"assets": ["css", "js", "img"]}
  if not os.path.exists(path):
    print(f"ERROR. Not found {path} or not exists.")
    return

  new_project =os.path.join(path, project_name)

  if not os.path.exists(new_project):
    os.mkdir(new_project)
    try:
      with open(os.path.join(new_project, 'index.html'), 'w') as xfile:
        xfile.write(html(project_name))
    except FileNotFoundError as err:
      print(err)

    for folder in folders["assets"]:
      new_directory = os.path.join(new_project, list(folders.keys())[0], folder)
      if folder and not os.path.exists(new_directory):
        os.makedirs(os.path.join(new_directory))
        if folder == "css":
          try:
              with open(os.path.join(new_directory, 'style.css'), 'w') as xfile:
                xfile.write(css('Roboto'))
          except FileNotFoundError as err:
            print(err)
        elif folder == "js":
          try:
              with open(os.path.join(new_directory, 'script.js'), 'w') as xfile:
                xfile.write(js())
          except FileNotFoundError as err:
            print(err)
    os.startfile(os.path.join(new_project, 'index.html'))
    os.system(f'code "{new_project}"')
    

# user = os.getenv("UserProfile")
# desktop = user+"\\Desktop"

# makeVoidProject(desktop, "nuevo")
from bs4 import BeautifulSoup


html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="/static/style.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <title>Cards</title>
</head>
<body>
    <div class="intro">
        <h1>Champions</h1>
    </div>
    <div class="box-card">
  
    {%for i in cards%}
    <div class="card" style="width: 18rem;">
        <img class="img" src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{{i.nome}}_{{indice}}.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h2 class="card-title">{{i.nome}}</h5>
          <p class="card-text">{{i.descricao}}</p>
          <p>
            <span class="material-symbols-outlined">
            swords
            </span> atk: {{i.atk}}
            <span class="material-symbols-outlined">
                security
            </span> def: {{i.df}}</p>
          <div>
            <button class="btn btn-danger"><a href="/delete/{{i.id}}">Deletar</a></button>
            <button class="btn btn-warning"><a href="/edit/{{i.id}}">Update</a></button>
          </div>
          <button class="mudar"> Mudar Skin</button>

        </div>
    </div>
    {%endfor%}
    </div>
    <div>
        <button type="button" class="btn btn-info"><a href="/add">ADD</a></button>
    </div>
   
    
</body>
</html>
"""


"""
def mudar():
    soup = BeautifulSoup(html_doc,'html.parser')
    mudar = soup.find('button',class_="mudar")
    mudar['onclick']= 'document.ElementByClassName("img").src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{{i.nome}}_1.jpg'
    return mudar
    """


from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def homepage():
    return 'bem-vindo a pagina inicial, digite "/formulario" para começar' 

@app.route('/formulario', methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        idade = request.form.get("idade")
        altura = request.form.get("altura")
        peso = request.form.get("peso")
        sexo = request.form.get("sexo")
        return f'Você é {name} {surname}, seu email é {email}, sua idade é {idade}Anos, sua altura é {altura}, seu peso é {peso}, seu sexo é {sexo}'
    
    return """
      <form method="POST">
      Nome: <input type="text" name="name"><br><br>
      Sobrenome: <input type="text" name="surname"><br><br>
      Email: <input type="email" name="email"><br><br>
      Idade: <input type="number" name="idade"><br><br>
      Altura: <input type="text" name="altura"><br><br>
      Peso: <input type="text" name="peso"><br><br>
      Sexo: <input type="text" name="sexo"><br><br>
      <input type="submit" value="Enviar">
      </form>
    """

if __name__ == '__main__':
    app.run(debug=True)
# cd formulario, cd flask, python3 main.py
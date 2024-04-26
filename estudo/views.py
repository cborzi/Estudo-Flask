from flask import render_template, url_for

from estudo import app


@app.route('/')
def homepage():
    usuario = 'Carlos'
    idade = 56

    context = {
        'usuario' : usuario,
        'idade' : idade
    }

    return render_template('index.html', context=context)

@app.route('/contato')
def novapag():
    return 'Nova página - outra view'

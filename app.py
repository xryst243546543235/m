from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    user = {'username': 'yURA'}
    return render_template('index.html', user=user)


@app.route('/help/')
def help():
    return '<h1>Мы уже выехали </h1>'


@app.route('/table/')
def t1():
    return '''
<table  border="1" width="100%" cellpadding="5">  
<caption>Перечень продуктов</caption>
  <tr>
    <th>№ п/п</th>
    <th>Наименование товара</th>
    <th>Ед. изм.</th>
    <th>Количество</th>
    <th>Цена за ед. изм., руб.</th>
    <th>Стоимость, руб.</th>
  </tr>
  <tr>
    <td>1.</td>
    <td>Томаты свежие</td><td>кг</td><td>15,20</td><td>69,00</td><td>1048,80</td>
  </tr>
  <tr>
    <td>2.</td>
    <td>Огурцы свежие</td><td>кг</td><td>2,50</td><td>48,00</td><td>120,00</td>
  </tr>
  <tr>
    <td colspan="5" style="text-align:right">ИТОГО:</td><td>1168,80</td>
  </tr>
</table>
'''


if __name__ == '__main__':
    app.run(debug=True)
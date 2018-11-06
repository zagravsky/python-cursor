page = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf8"/>
    <link rel="stylesheet" href="bootstrap.min.css"/>
  </head>
  <body>
    <h1>Книга учёта</h1>
    <h2>Расходы за {date}</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">Продукт</th>
          <th scope="col">Количество</th>
          <th scope="col">Единица</th>
          <th scope="col">Цена, грн/eд.</th>
          <th scope="col">Стоимость, грн</th>
        </tr>
      </thead>
      <tbody>
        {table_rows}
      </tbody>
      <tfoot>
        <tr>
          <th colspan="4" scope="row">Итого</th>
          <th>{total_cost}</th>
        </tr>
      </tfoot>
    </table>
  </body>
</html>'''

table_row = '''<tr>
  <td>{item}</td>
  <td>{quantity}</td>
  <td>{unit}</td>
  <td>{price}</td>
  <td>{cost}</td>
</tr>'''

# комментарий

print("всем привет!")
print('всем привет')
print('два', 'один')

a = 9
print(a)
name = input("ведите свое имя :")

print()

a = int(input("Введите первое число :"))
b = int(input("Введите второе число :"))

z = input("введите знак :")

if z == "+" :
    print(a + b)
elif z == "-" :

    print(a - b)
elif z == "*" :
    print(a * b)
elif z == "/":
    print(a / b)
else:
    print("ошибка")

#website

from flask import Flask, request, render_template

app = Flask(website)


@app.route('/')
def hello_world():
    """
    -1
    -2
    -3
    -4
    -5
    -6
    """
    return 'Hello World!'


@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = None
    return render_template('hello_form.html', name=name)


@app.route('/<name>')
def hello_buddy(name):
    return 'Hello, ' + name + '!'


if __name__ == '__main__':
    app.run()
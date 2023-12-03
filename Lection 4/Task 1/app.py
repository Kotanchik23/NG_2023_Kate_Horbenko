from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/ask")
def ask():
    return render_template("ask.html")

@app.route("/result")
def result():
    def add(valuea, valueb):
        return valuea + valueb
    def sub(valuea, valueb):
        return valuea - valueb
    def mul(valuea, valueb):
        return valuea * valueb
    def div(valuea, valueb):
        if valueb == 0:
            return "Division by zero is impossible"
        return valuea / valueb
    def square_root(valuea):
        if valuea < 0:
            return "You can't take the root of a negative number"
        return valuea ** (1 / valueb)
    def power(valuea, valueb):
        return valuea ** valueb

    valuea = float(request.args.get("valuea"))
    valueb = float(request.args.get("valueb"))
    ope = int(request.args.get("operation"))
    
    if ope == 1:
        result = add(valuea, valueb)
    elif ope == 2:
        result = sub(valuea, valueb)
    elif ope == 3:
        result = mul(valuea, valueb)
    elif ope == 4:
        result = div(valuea, valueb)
    elif ope == 5:
        result = square_root(valuea)
    elif ope == 6:
        result = power(valuea, valueb)
    return render_template("result.html", res = result)

@app.route("/")
def index():
    return render_template("index.html", data="Test")

if __name__ == '__main__':
    app.run(debug=True)
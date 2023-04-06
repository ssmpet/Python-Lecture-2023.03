from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
        <h1>Hellow World!!!</h1>
        <hr>
        <p>디버그 모드에서는 변경 사항이 발생하면 자동적으로 서버가 재실행됩니다.</p>
    '''

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/clock')
def clock():
    return render_template('clock.html')

if __name__ == '__main__':
    app.run(debug=True)
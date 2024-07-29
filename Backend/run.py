from flask import Flask, Response, render_template
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    def generate():
        data = ['data1', 'data2', 'data3']  # Your data array
        for item in data:
            yield f'data: {item}\n\n'
            time.sleep(1)  # Pause between data chunks
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
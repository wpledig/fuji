from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    return ""


if __name__ == '__main__':
    app.run()
from src import App
from waitress import serve

if __name__ == '__main__':
    serve(App, host="0.0.0.0", port=5000)
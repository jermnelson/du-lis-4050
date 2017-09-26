__author__ = "Jeremy Nelson"

from app import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5707)

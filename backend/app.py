from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine(
    "mysql+pymysql://root:dnyanu@2027@localhost/banking_db"
)

@app.route('/')
def home():
    return "Database Connected"

if __name__ == "__main__":
    app.run(debug=True)
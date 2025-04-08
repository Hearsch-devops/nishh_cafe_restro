from flask import Flask, request, render_template
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        full_name = request.form.get('booking-form-name')
        phone = request.form.get('booking-form-phone')
        time = request.form.get('booking-form-time')
        date = request.form.get('booking-form-date')
        number = request.form.get('booking-form-number')
        message = request.form.get('booking-form-message')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO reservations (full_name, phone, reservation_time, reservation_date, number_of_people, message)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (full_name, phone, time, date, number, message))

        conn.commit()
        cur.close()
        conn.close()

        return "Reservation submitted successfully!"
    return render_template('reservation.html')

if __name__ == '__main__':
    app.run(debug=True)

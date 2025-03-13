from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database connection function
def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Anant@1080",
        database="myproject"
    )

# Homepage route (list all students or provide update link)
@app.route('/')
def home():
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template("index.html", students=students)

# Student update route (specific to a student's ID)
@app.route('/update/<int:student_id>', methods=["GET", "POST"])
def update_student(student_id):
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    # Fetch current student data
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        course = request.form['course']
        contact = request.form['contact']
        
        # Update student data in the database
        cursor.execute("""
            UPDATE students 
            SET name = %s, age = %s, gender = %s, course = %s, contact = %s 
            WHERE id = %s
        """, (name, age, gender, course, contact, student_id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('home'))  # Redirect back to home after updating
    
    conn.close()
    return render_template("update.html", student=student)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
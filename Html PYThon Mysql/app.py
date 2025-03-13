from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key

def connect_db():
    return pymysql.connect(host='localhost', user='root', password='sumit', db='studentdb')

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = connect_db()
        cursor = connection.cursor()

        # Debug statement
        print(f"Trying to login with username: {username}")

        cursor.execute("SELECT id, username, password, role FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()
        connection.close()

        # Check if the user exists and compare the plain text password
        if user and user[2] == password:
            session['user_id'] = user[0]
            if user[3] == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif user[3] == 'student':
                return redirect(url_for('student_dashboard'))
        else:
            flash('Invalid username or password. Please try again.')

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        connection = connect_db()
        cursor = connection.cursor()
        
        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash('Username already taken. Please choose another username.')
        else:
            try:
                cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, 'student')", (username, password))
                connection.commit()
                flash('Account created successfully. Please log in.')
                return redirect(url_for('login'))
            except pymysql.MySQLError as e:
                flash('An error occurred while creating your account. Please try again.')
                print(f"Database error: {e}")
        
        connection.close()
    
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user_id from the session
    return redirect(url_for('login'))

@app.route('/admin_dashboard')
def admin_dashboard():
    try:
        if 'user_id' not in session or not is_admin(session['user_id']):
            return redirect(url_for('login'))
        return render_template('admin_dashboard.html')
    except Exception as e:
        print(f"Error in admin_dashboard: {e}")
        return "An error occurred. Please try again later."

@app.route('/student_dashboard')
def student_dashboard():
    try:
        if 'user_id' not in session or is_admin(session['user_id']):
            return redirect(url_for('login'))
        return render_template('student_dashboard.html')
    except Exception as e:
        print(f"Error in student_dashboard: {e}")
        return "An error occurred. Please try again later."

@app.route('/add_subject', methods=['GET', 'POST'])
def add_subject():
    if 'user_id' not in session or not is_admin(session['user_id']):
        return redirect(url_for('login'))

    if request.method == 'POST':
        subject_names = request.form.getlist('subject_name[]')  # Get multiple subjects as a list
        connection = connect_db()
        cursor = connection.cursor()
        try:
            for subject_name in subject_names:
                cursor.execute("INSERT INTO subjects (subject_name) VALUES (%s)", (subject_name,))
            connection.commit()
            flash('Subjects added successfully.')
        except pymysql.MySQLError as e:
            connection.rollback()
            flash('An error occurred while adding subjects. Please try again.')
            print(f"Database error: {e}")
        finally:
            connection.close()

        return redirect(url_for('admin_dashboard'))

    return render_template('add_subject.html')

@app.route('/add_marks', methods=['GET', 'POST'])
def add_marks():
    if 'user_id' not in session or not is_admin(session['user_id']):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        student_id = request.form['student_id']
        connection = connect_db()
        cursor = connection.cursor()

        try:
            # Loop through the submitted form data and extract the marks for each subject
            for subject_id in request.form.getlist('subject_id'):
                marks = request.form.get(f'marks_{subject_id}')
                
                if marks:  # If marks were provided for this subject
                    cursor.execute("INSERT INTO marks (student_id, subject_id, marks) VALUES (%s, %s, %s)", (student_id, subject_id, marks))
            
            connection.commit()
            flash('Marks added successfully.')
        except pymysql.MySQLError as e:
            connection.rollback()
            flash('An error occurred while adding marks. Please try again.')
            print(f"Database error: {e}")
        finally:
            connection.close()
        
        return redirect(url_for('admin_dashboard'))
    
    # Query students and subjects from the database for the dropdown
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM students")  # Fetch all students
    students = cursor.fetchall()
    cursor.execute("SELECT id, subject_name FROM subjects")  # Fetch all subjects
    subjects = cursor.fetchall()
    connection.close()
    
    return render_template('add_marks.html', students=students, subjects=subjects)

@app.route('/view_result', methods=['GET', 'POST'])
def view_result():
    if request.method == 'POST':
        roll_number = request.form['roll_number']

        connection = connect_db()
        cursor = connection.cursor()

        # Fetch student ID based on the roll number
        cursor.execute("SELECT id, name FROM students WHERE roll_number = %s", (roll_number,))
        student = cursor.fetchone()

        if student:
            student_id = student[0]
            student_name = student[1]

            # Fetch the subjects and marks for the student
            cursor.execute("""
                SELECT subjects.subject_name, marks.marks
                FROM marks
                JOIN subjects ON marks.subject_id = subjects.id
                WHERE marks.student_id = %s
            """, (student_id,))
            results = cursor.fetchall()

            connection.close()

            if results:
                return render_template('view_result.html', student_name=student_name, results=results)
            else:
                flash("No marks found for this student.", "warning")
                return redirect(url_for('view_result'))
        else:
            flash("Roll number not found.", "danger")
            return redirect(url_for('view_result'))

    return render_template('view_result.html')

def is_admin(user_id):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT role FROM users WHERE id=%s", (user_id,))
        result = cursor.fetchone()
        if result:
            return result[0] == 'admin'
        return False
    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
        return False
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change the port number if needed

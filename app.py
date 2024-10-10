from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Register the user
        return redirect(url_for('login'))
    return render_template('register.html', title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login
        return redirect(url_for('patient_entry'))
    return render_template('login.html', title='Login')

@app.route('/patient_entry', methods=['GET', 'POST'])
def patient_entry():
    if request.method == 'POST':
        # Save patient details
        return redirect(url_for('predict'))
    return render_template('patient_entry.html', title='Patient Entry')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction_result = None
    if request.method == 'POST':
        # Get the prediction from the model
        prediction_result = 'Positive'  # Dummy result
    return render_template('predict.html', title='Predict', prediction_result=prediction_result)

@app.route('/report')
def report():
    return render_template('report.html', title='Report')

if __name__ == '__main__':
    app.run(debug=True)

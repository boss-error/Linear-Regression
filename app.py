from flask import Flask, render_template, request, flash
from utils.linear_regression import calculate_linear_regression
from utils.latex_generator import generate_latex_output
import numpy as np

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            x_input = request.form.getlist('x')
            y_input = request.form.getlist('y')
            predict_value = float(request.form['predict_value'])
            
            x = np.array([float(i) for i in x_input])
            y = np.array([float(i) for i in y_input])
            
            results = calculate_linear_regression(x, y, predict_value)
            table_latex, equations_latex, steps_latex, result_latex = generate_latex_output(results)
            
            return render_template('result.html',
                                table_latex=table_latex,
                                equations_latex=equations_latex,
                                steps_latex=steps_latex,
                                result_latex=result_latex)
        except ValueError:
            flash('Error: Please ensure all inputs are valid numbers', 'error')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
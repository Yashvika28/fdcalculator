from flask import Flask, request, render_template_string

app = Flask(__name__)

# Combined HTML and CSS template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FD Calculator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, serif;
            background-color: #D3D3D3;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: white;
            padding: 2em;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 400px;
        }
        h1 {
            margin-bottom: 20px;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 1em;
        }
        input {
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .result {
            margin-top: 20px;
        }
        .result h2 {
            color: #333;
        }
        .error {
            color: red;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Fixed Deposit Calculator</h1>
        
        {% if error %}
        <p class="error">{{ error }}</p>
        {% endif %}
        
        <form action="/" method="POST">
            <label for="principal">Principal Amount:</label>
            <input type="number" name="principal" id="principal" required step="any" placeholder="Enter principal amount">

            <label for="rate_of_interest">Rate of Interest (% per annum):</label>
            <input type="number" name="rate_of_interest" id="rate_of_interest" required step="any" placeholder="Enter rate of interest">

            <label for="time_period">Time Period (in years):</label>
            <input type="number" name="time_period" id="time_period" required step="any" placeholder="Enter time period">

            <button type="submit">Calculate</button>
        </form>
        
        {% if maturity_amount %}
        <div class="result">
            <h2>Maturity Amount: ₹{{ maturity_amount }}</h2>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    maturity_amount = None

    if request.method == "POST":
        try:
            # Get data from the form
            principal = float(request.form["principal"])
            rate_of_interest = float(request.form["rate_of_interest"])
            time_period = float(request.form["time_period"])

            # Calculation for maturity amount
            maturity_amount = principal * (1 + (rate_of_interest / 100)) ** time_period
            maturity_amount = round(maturity_amount, 2)  # Round off to two decimal places
        except ValueError:
            error = "Please enter valid numeric inputs."

    return render_template_string(html_template, error=error, maturity_amount=maturity_amount)

if __name__ == "__main__":
    app.run(debug=True)

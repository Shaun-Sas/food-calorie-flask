import requests
from flask import render_template, Flask, request
from pathlib import Path
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv

load_dotenv(Path(f"{Path().absolute()}\env\.env"))
apikey = os.getenv("apikey")


print(f"Directory Path:" ,Path(f"{Path().absolute()}\env\.env"))
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    data = None
    error = None

    if request.method == 'POST':
        query = request.form.get('query')  # Get the user input from the form
        if query:
            api_url = f'https://api.calorieninjas.com/v1/nutrition?query={query}'
            response = requests.get(api_url, headers={'X-Api-Key': apikey})
            if response.status_code == requests.codes.ok:
                data = response.json().get('items', [])
            else:
                error = f"Error: {response.status_code}. Could not fetch data. Try again later."
        else:
            error = "Please enter a valid query."

    return render_template('index.html', data=data, error=error)

if __name__ == "__main__":
    app.run(debug=True)

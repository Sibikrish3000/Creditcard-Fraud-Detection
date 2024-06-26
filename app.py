from fastapi import FastAPI,Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import warnings
warnings.filterwarnings('ignore')
import joblib
import uvicorn
import zipfile
import os


app = FastAPI(title="Credit Card Fraud Detection API",
    description="""An API that utilises a Machine Learning model that detects a credit card transaction fraudulent""",
    version="1.0.0", debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Specify the path to the zip file
zip_file_path = 'model.zip'

# Specify the directory where you want to extract the files
extract_to_directory = 'model'

# Create the directory if it doesn't exist
os.makedirs(extract_to_directory, exist_ok=True)

try:
    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all the contents to the specified directory
        zip_ref.extractall(extract_to_directory)
    print(f"Files extracted to {extract_to_directory}")
except zipfile.BadZipFile:
    print("Error: The file is not a zip file or it is corrupted.")
except FileNotFoundError:
    print(f"Error: The file '{zip_file_path}' was not found.")
except PermissionError:
    print(f"Error: Permission denied while accessing '{zip_file_path}' or '{extract_to_directory}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


xgb_model = joblib.load('./model/xgb_model.pkl')
rf_model = joblib.load('./model/rf_model.pkl')
enc = joblib.load('./Encoder/WOEEncoder.pkl')


@app.get('/',response_class=HTMLResponse)
def running():
    text='''
    <html>
    <head>
    <link rel="icon" type="image/x-icon" href="static/images/api.png">
    <title>Credit Card Fraud Detection API</title>
    </head>
    <body>
    <div>
    <h1>Credit Card Fraud Detection API</h1>
        <a href="https://github.com/Sibikrish3000/">Github repository</a>
    </div>
    </body>
    </html>
    '''
    return text

class fraudinput(BaseModel):
    cc_freq:int
    cc_freq_class:int
    job:str
    age:int
    gender_M:int
    category:str
    distance_km:float
    hour:str
    hours_diff_bet_trans:int
    amt:float
@app.post('/predict')
async def predict(data: fraudinput,model:str =Query(...)):
    print('data: %s' % data)
    data=data.dict()
    enc_data=enc.transform([data])
    print('model:'+model)
    if model == 'xgboost':
        prediction=xgb_model.predict(enc_data)
    elif model == 'randomforest':
        prediction=rf_model.predict(enc_data)
    else:
        return {'error': 'Invalid model selected'}
    print("prediction:",prediction[0])
    return {"prediction":int(prediction[0])}

#if __name__ == '__main__':
    #uvicorn.run(app, host='127.0.0.1', port=8000)



    #uvicorn.run(app, host="0.0.0.0", port=8000)



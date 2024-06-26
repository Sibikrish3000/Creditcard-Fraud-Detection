import time
import gradio as gr
import requests
from features import category_names,job_names
from PIL import Image
#import uvicorn
#import threading
#from app import app
#import psutil


def close_port(port):
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port:
            print(f"Closing port {port} by terminating PID {conn.pid}")
            process = psutil.Process(conn.pid)
            process.terminate()


"""
def run_fastapi():
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        print(f'Error running fastapi:{e}')
        close_port(8000)


fastapi_thread = threading.Thread(target=run_fastapi)
fastapi_thread.daemon = True
fastapi_thread.start()
time.sleep(2)
"""

def predict_fraud(cc_freq, job, age, gender_M, category, distance_km, hour, hours_diff_bet_trans, amt, model):
    def map_time_of_day(hour):
        if 0 <= hour <= 4:
            return 'night'
        elif 5 <= hour <= 11:
            return 'morning'
        elif 12 <= hour <= 20:
            return 'afternoon'
        else:
            return 'night'

    def cc_freq_classes(x):
        for idx, val in enumerate(list(range(800, 10000, 800))):
            if x < val:
                return idx + 1

    cc_freq_class=cc_freq_classes(cc_freq)
    hour = map_time_of_day(hour)

    input_data = {
        'cc_freq': cc_freq,
        'cc_freq_class': cc_freq_class,
        'job': job,
        'age': age,
        'gender_M': 1 if gender_M == 'Male' else 0,
        'category': category,
        'distance_km': distance_km,
        'hour': hour,
        'hours_diff_bet_trans': hours_diff_bet_trans,
        'amt': amt
    }

    try:
        response = requests.post(f'http://0.0.0.0:8000/predict?model={model.lower()}', json=input_data)
        response.raise_for_status()
        if response.status_code == 200:
            prediction = response.json()
            return 'This Transaction is legitimate.' if prediction['prediction'] == 0 else 'This Transaction is not legitimate.'
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Define the input components
theme = gr.themes.Base(
    primary_hue="teal",
    neutral_hue="sky",
    radius_size="lg",
).set(
    body_text_weight='300',
    shadow_drop_lg='*button_shadow_hover',
    shadow_inset='*shadow_drop_lg'
)

js= """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';

    var text = 'Credit Card Fraud Detection';
    var totalDuration = 2000; // Total duration for the whole animation
    var animationDelay = totalDuration / text.length; // Delay between each letter animation

    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.7s ease-in-out'; // Smoother transition
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * animationDelay); // Use calculated delay
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}

"""

callback = gr.CSVLogger()
default_img=Image.open('static/images/creditcard.jpg')
with gr.Blocks(theme=theme,js=js) as interface:

    gr.Image( value=default_img,show_download_button=False)
    with gr.Tab('predict',):
        with gr.Row():
            with gr.Column():
                cc_freq = gr.Number(label="Credit Card Frequency")
                job = gr.Dropdown(job_names, label="Job")
                age = gr.Slider(minimum=0, maximum=100, step=1, label="Age")
                gender_M = gr.Radio(['Male', 'Female'], label="Gender")
                category = gr.Dropdown(category_names, label="Category")
                distance_km = gr.Number(label="Distance (km)")
                hour = gr.Slider(minimum=0, maximum=24, step=1, label="Hour")
                hours_diff_bet_trans = gr.Number(label="Hours Difference Between Transactions")
                amt = gr.Number(label="Amount")
                model_choice = gr.Radio(['XGBoost', 'RandomForest'], label="Choose Model", )
            with gr.Column():
                output = gr.Label(label="Prediction")
                with gr.Row():
                    predict_button = gr.Button("Predict")
                    flag_button = gr.Button('Flag')

        callback.setup([cc_freq, job, age, gender_M, category, distance_km, hour, hours_diff_bet_trans, amt, model_choice],
                       "log")

        predict_button.click(fn=predict_fraud,
                             inputs=[cc_freq, job, age, gender_M, category, distance_km, hour, hours_diff_bet_trans, amt,
                                     model_choice], outputs=output)
        flag_button.click(lambda *args: callback.flag(args),
                          [cc_freq, job, age, gender_M, category, distance_km, hour, hours_diff_bet_trans, amt,
                           model_choice], None, preprocess=False)
    with gr.Tab('About'):
        with open('about.md', 'r') as about:
            gr.Markdown(about.read(),line_breaks=True,header_links=True)



if __name__ == "__main__":
    interface.launch(share=True)
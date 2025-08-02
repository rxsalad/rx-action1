import os
import uuid
from flask import Flask,request

from dotenv import load_dotenv
 
load_dotenv()

# create the .env file
PASSWORD_TEST = os.getenv("PASSWORD_TEST","")
NUMBER_TEST = int(os.getenv("NUMBER_TEST", "111"))

print(PASSWORD_TEST)
print(NUMBER_TEST)


app = Flask(__name__)

count_hc = 0
count_prediction = 0
machine_id = str(uuid.uuid4())


@app.route('/')
def main():
    return {"STATUS":"OK"}


@app.route('/hc')
def health():
    global count_hc
    count_hc = count_hc + 1
    temp = 'machine_id:{}, hc:{}, prediction:{}'.format(machine_id,count_hc,count_prediction)
    print(temp)
    return {"STATUS":temp}


@app.route('/prediction', methods=['GET', 'POST'])
def hello_world():
    global count_prediction
    count_prediction = count_prediction + 1

    if request.method == "GET":
        temp = 'machine_id:{}, hc:{}, prediction:{}'.format(machine_id,count_hc,count_prediction)
    else:
        job_id = request.form.get('job_id')
        temp = 'jod_id:{}, machine_id:{}, hc:{}, prediction:{}'.format(job_id,machine_id,count_hc,count_prediction)

    print(temp)
    return temp

if __name__ == '__main__':
#   app.run(host="0.0.0.0", port = 8888)
    app.run(host="::", port = 8888) 
    
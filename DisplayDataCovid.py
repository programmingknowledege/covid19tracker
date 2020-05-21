import requests
from flask import *
import json
app = Flask(__name__)
@app.route("/")
def home():
    uri = "https://api.covid19india.org/state_district_wise.json"
    content = requests.get(uri)
    Jresponse = content.text
    data = json.loads(Jresponse)
    confirmed = 0
    active = 0
    recovered = 0
    liststates = []
    listconfirmed = []
    listactive = []
    listrecovered = []
    for i in data.items():
        x = i[1]
        liststates.append(i[0])
        for j in i[1].items():
            z = j[1]
            if type(z) is dict:
                confirmedd = 0;
                activee = 0;
                recoveredd = 0
                for k in z.items():
                    dataa = k[1]
                    confirmed = confirmed + dataa["confirmed"]
                    active = active + dataa["active"]
                    recovered = recovered + dataa["recovered"]
                    confirmedd = confirmedd + dataa["confirmed"]
                    activee = activee + dataa["active"]
                    recoveredd = recoveredd + dataa["recovered"]
                listconfirmed.append(confirmedd)
                listactive.append(activee)
                listrecovered.append(recoveredd)
    return render_template("DisplayData.html", confirmed=confirmed, active=active, recovered=recovered, liststates=liststates,
                           listconfirmed=listconfirmed, listactive=listactive, listrecovered=listrecovered,n=len(liststates))


if __name__ == '__main__':
    app.run(debug=True)

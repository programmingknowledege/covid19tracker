import requests
from flask import *
import json

app = Flask(__name__)

uri = "https://api.covid19india.org/state_district_wise.json"
content = requests.get(uri)
Jresponse = content.text
data = json.loads(Jresponse)


@app.route("/")
def home():
    confirmed = 0
    active = 0
    recovered = 0
    liststates = []
    listconfirmed = []
    listactive = []
    listrecovered = []
    for a, b in data.items():
        liststates.append(a)
        for c, d in b.items():
            if type(d) is dict:
                confirmedd = 0;
                activee = 0;
                recoveredd = 0
                for e, f in d.items():
                    confirmed = confirmed + f["confirmed"]
                    active = active + f["active"]
                    recovered = recovered + f["recovered"]
                    confirmedd = confirmedd + f["confirmed"]
                    activee = activee + f["active"]
                    recoveredd = recoveredd + f["recovered"]
                listconfirmed.append(str(confirmedd))
                listactive.append(str(activee))
                listrecovered.append(str(recoveredd))

    return render_template("DisplayData.html", confirmed=confirmed, active=active, recovered=recovered,
                           liststates=liststates,
                           listconfirmed=listconfirmed, listactive=listactive, listrecovered=listrecovered,
                           n=len(liststates))


@app.route("/districtwise")
def districtdata():
    confirmed = 0
    active = 0
    recovered = 0
    liststates = []
    for i in data.items():
        x = i[1]
        liststates.append(i[0])
        for j in i[1].items():
            z = j[1]
            if type(z) is dict:
                for k in z.items():
                    dataa = k[1]
                    confirmed = confirmed + dataa["confirmed"]
                    active = active + dataa["active"]
                    recovered = recovered + dataa["recovered"]

    listdistrict = []
    listconfirmed = []
    listactive = []
    listrecovered = []
    for a, b in data.items():
        for c, d in b.items():
            if type(d) is dict:
                for a, b in d.items():
                    listdistrict.append(a)
                    listconfirmed.append(b["confirmed"])
                    listactive.append(b["active"])
                    listrecovered.append(b["recovered"])

    return render_template("districtdata.html", confirmed=confirmed, active=active, recovered=recovered,
                           listdistrict=listdistrict,
                           listconfirmed=listconfirmed, listactive=listactive, listrecovered=listrecovered,
                           n=len(listdistrict))


@app.route("/About")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)

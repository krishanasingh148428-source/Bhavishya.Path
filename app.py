from flask import Flask, render_template, request, session, redirect, url_for, abort
from data import STREAMS, CAREERS, STREAM_NAMES
from gyani import reply

app = Flask(__name__)
app.secret_key = "bhavishyapath-secret-key"

@app.route("/")
def home():
    return render_template("home.html", streams=STREAMS, n=len(CAREERS))

@app.route("/stream/<key>")
def stream(key):
    s = STREAMS.get(key) or abort(404)
    if len(s[3]) == 1:
        return redirect(url_for("careers", key=key, i=0))
    return render_template("pick.html", key=key, s=s)

@app.route("/careers/<key>/<int:i>")
def careers(key, i):
    s = STREAMS.get(key) or abort(404)
    if i >= len(s[3]):
        abort(404)
    label, code, ex = s[3][i]
    q = request.args.get("q", "").lower()
    mn = float(request.args.get("min") or 0)
    lst = [c for c in CAREERS if code in c["streams"] and c["name"] not in ex
           and q in (c["name"] + c["path"] + c["scope"]).lower() and c["hi"] >= mn]
    if request.args.get("sort") == "salary":
        lst.sort(key=lambda c: -c["hi"])
    return render_template("careers.html", key=key, i=i, s=s, label=label, lst=lst)

@app.route("/career/<int:cid>")
def career(cid):
    if cid >= len(CAREERS):
        abort(404)
    return render_template("detail.html", c=CAREERS[cid], sn=STREAM_NAMES)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        m = request.form.get("m", "").strip()
        if m:
            session["h"] = (session.get("h", []) + [["you", m], ["baba", reply(m)]])[-20:]
        return redirect(url_for("chat"))
    return render_template("chat.html", h=session.get("h", []))

@app.route("/chat/clear")
def clear():
    session.pop("h", None)
    return redirect(url_for("chat"))

if __name__ == "__main__":
    app.run(debug=True)

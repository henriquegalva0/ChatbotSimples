from flask import Flask, render_template, request
from callbot import generate_answer

app = Flask(__name__)


chat_history=[{"role":"User","content":"input"},{"role":"Bot","content":"output"}]
user_input=""

@app.route("/",methods=["GET","POST"])
def index():

    global user_input, chat_history

    if request.method=="POST":

        user_input=request.form.get("user_input")
        chat_history=generate_answer(user_input,chat_history)

    return render_template("index.html", display=chat_history)
    
if __name__ == "__main__":
    app.run(debug=True)
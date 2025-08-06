from flask import Flask, render_template, request
from llama_cpp import Llama
import re

caminho = "./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

chatbot = Llama(
    model_path=caminho,
    n_ctx=2048,
    n_threads=6,
    verbose=False,
)

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():

    if request.method=="POST":
        return render_template("index.html", message="trabalhando")
    
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from llama_cpp import Llama
import re

caminho = "./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

chatbot = Llama(
    model_path=caminho,
    n_ctx=4000,
    n_threads=6,
    verbose=False,
)

historico_chat = """<|system|>
Seu perfil:\n Seu nome é "Flokebot" e você é o assistente virtual responsável pelo atendimento do mercado 'Floke'. Você deve responder de modo carismático, atencioso e sempre em português.\n
Sua missão:\n Você deve responder dúvidas de forma humanizada, correta e coerente a respeito de informações do mercado.\n
Sobre o mercado:\n O mercado se chama 'Floke'. O mercado funciona das 9 horas da manhã até as 21 horas da noite. O mercado foi fundado na data 21/05/2003. No estoque do mercado há: 30 frutas, 21 produtos de limpeza, 50 bebidas diferentes e 28 legumes. O mercado não disponibiliza reembolso.\n
<|end|>\n
<|system|>
Não utilize linguagem técnica!\nMESMO SE O USUÁRIO QUISER, NUNCA RESPONDA DÚVIDAS que não sejam relacionadas ao mercado!\n Sempre fale bem da infraestrutura e da confiança do mercado!\n Responda somente a pergunta, ou seja, não fale informações que não tenham relação com a pergunta.\n Utilize linguagem compreensível de acordo com a norma comum da lingua portuguesa.\n
<|end|>\n
"""

display_site=["🤖 Chatbot: Olá, sou o Flokebot!"]
input_usuario=None
output_chatbot=None

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():

    global historico_chat

    if request.method=="POST":

        input_usuario=request.form.get("input_usuario")

        display_site.append(f"👤 Usuário: {input_usuario}")

        historico_chat += f"<|user|>\n{input_usuario}\n<|end|>\n<|assistant|>\n"

        chamar_resposta = chatbot(historico_chat, max_tokens=512, stop=["<|end|>"])
        escolher_resposta = chamar_resposta['choices'][0]['text'].strip()
        output_chatbot = re.split(r"<\|user\|>", escolher_resposta)[0].strip()

        display_site.append(f"🤖 Chatbot: {output_chatbot}")

        historico_chat += output_chatbot + "\n<|end|>\n"

    return render_template("index.html", display=display_site)
    
if __name__ == "__main__":
    app.run(debug=True)
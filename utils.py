from llama_cpp import Llama

model_path = "./models/deepseek-llm-7b-chat.Q5_K_M.gguf"

llm = Llama(
    model_path=model_path,
    n_ctx=2048,
    n_threads=8,
    verbose=True,
)

chat_history=[]
user_input="What is Pi in the math context?"

chat_history.append({"role":"user","content":user_input})

gen_output=llm.create_chat_completion(
    messages=chat_history,
    temperature=0.45,
    top_p=0.95,
)

bot_output=gen_output["choices"][0]["message"]["content"]
chat_history.append({"role":"assistant","content":bot_output})

for key,item in chat_history.items():
    print(f"{key}: ",item,end="\n")
from llama_cpp import Llama

def generate_answer(user_input,chat_history):

    if user_input == " " or user_input == "":
        return chat_history
    else:
        model_path = "./models/deepseek-llm-7b-chat.Q5_K_M.gguf"

        llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=8,
            verbose=True,
        )

        chat_history.append({"role":"user","content":user_input})

        gen_output=llm.create_chat_completion(
            messages=chat_history,
            temperature=0.45,
            top_p=0.95,
        )

        bot_output=gen_output["choices"][0]["message"]["content"]
        chat_history.append({"role":"bot","content":bot_output})

        return chat_history
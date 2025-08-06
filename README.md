# Projeto
Estou elaborando meu primeiro chatbot utilizando um modelo [Mistral](https://mistral.ai/models), o qual funciona por meio da elaboração de prompts bem definidos. O modelo pode apresentar falhas por falta de suporte ao português ou limitações do modelo, **haja vista que é um projeto teste**.

## Percurso
Comecei o projeto visando usar grandes modelos de linguagem para desenvolver o chatbot direto do [HuggingFace](https://huggingface.co/). O primeiro deles foi o *[DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1)* que demonstrou uma perfomance excepcional, porém extremamente custosa computacionalmente. Após isso, utilizei o modelo transformer *[BERT](https://huggingface.co/neuralmind/bert-base-portuguese-cased)*, no entanto ele não funcionava precisamente para o que eu necessitava.

Finalmente, decidi selecionar um modelo específico da [Mistral](https://mistral.ai/models) e obtive resultados extremamente satisfatórios. O retorno dado pelo chatbot apresentou poucas falhas que podem ser previstas facilmente pela **estruturação de um prompt superior**.

Com isso, é possível demonstrar que, atualmente, **com pouco hardware e poucas linhas de código** já é possível arquitetar um chatbot LLM razoável capaz de resolver problemas baseado em comandos.

## Chatbot
Criei um cenário imaginário de um mercado chamado *Floke* que recentemente adquiriu a tecnologia dos chatbots e implementou o *Flokebot* - um assistente digital para atendimento de clientes online. Dentro desse contexto, criei brevemente um prompt no arquivo [utils.py](utils.py) somente para mostrar a capacidade e funcionalidade do chatbot.

### Especificações
O modelo escolhido foi o *[mistral-Q4KM](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/tree/main)* no formato *[GGUF](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md)*, que **não está localizado na pasta [models](models/)** para evitar acréscimo de peso ao repositório.

É posssível utilizar métodos como *[RAG](https://github.com/NirDiamant/RAG_Techniques)* para aumentar o leque de informações que podem ser passadas ao bot para expandir sua janela de contexto.

### Funcionamento
- O arquivo [utils.py](utils.py) contém uma simples demontração do chatbot para testes rápidos.
- O arquivo [app](app.py) traz uma aplicação do chatbot em site flask simples.
- O arquivo [requirements.txt](requirements.txt) lista as bibliotecas e frameworks utilizadas no projeto.
- O arquivo [index.html](templates/index.html) é a base de conexão do HTML com os arquivos carregados pelo flask.
- A pasta [models](models/) está vazia, porém é feita para armazenar o modelo *[mistral-Q4KM](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/tree/main)*.

### Parâmetros
Os parâmetros vitais do modelo são:

  *n_ctx=2048* -> Janela de contexto, isto é, qual a quantia **máxima dos tokens** da soma do histórico da conversa, input do usuário e output do chatbot.
  *n_threads=6* -> Quantia de núcleos utilizados em sua CPU. (6 é um uso equilibrado e 8~12 é mais rápido, porém custoso)

Esses parâmetros modificam conforme o seu objetivo e o seu hardware. Estou utilizando um processador I5-9400F e dentro desse espectro, essa quantia de threads é equilibrada.

### Recomendações
[Modelos quantizados](https://github.com/Efficient-ML/Awesome-Model-Quantization) são sempre bem-vindos. Além disso, **use GPU para o processamento** (tenho uma placa de vídeo da amd, logo isso não é possível para mim).

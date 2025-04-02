
# Sarah - Assistente Virtual Multiplataforma 🤖

Sarah é uma assistente virtual carismática e versátil, desenvolvida para interagir através de múltiplas plataformas de comunicação, incluindo Discord, Telegram e uma API REST.

## 🌟 Características

- **Personalidade Única**: Sarah possui uma personalidade cativante, equilibrando profissionalismo e simpatia
- **Multi-plataforma**: Disponível no Discord, Telegram e via API REST
- **Memória Contextual**: Capaz de manter contexto das conversas
- **API Flexível**: Endpoint REST para integração com outros sistemas
- **Resposta Natural**: Utiliza LLM (Large Language Model) para respostas naturais e contextualizadas

## 🛠️ Tecnologias Utilizadas

- Python 3.11+
- Discord.py
- Flask
- Telegram Bot API
- LangChain
- OpenRouter API

## 📦 Estrutura do Projeto

```
├── sarah/
│   ├── core.py         # Núcleo de processamento da Sarah
│   ├── memory.json     # Arquivo de memória
│   └── memory.py       # Gerenciamento de memória
├── keep_alive.py       # Servidor web para manter o bot online
├── main.py            # Bot do Discord
└── telegram_bot.py    # Bot do Telegram
```

## 🚀 Como Executar

1. Configure as variáveis de ambiente necessárias:
   - `DISCORD_TOKEN`: Token do bot do Discord
   - `TELEGRAM_TOKEN`: Token do bot do Telegram
   - `OPENROUTER_API_KEY`: Chave da API OpenRouter

2. Execute o bot principal:
   ```bash
   python main.py
   ```

## 🔌 API REST

### Endpoint
- **POST** `/respond`
  - Recebe perguntas e retorna respostas da Sarah
  - Corpo da requisição (JSON):
    ```json
    {
        "question": "Sua pergunta aqui"
    }
    ```
  - Resposta:
    ```json
    {
        "reply": "Resposta da Sarah"
    }
    ```

## 🤝 Contribuição

Este é um projeto em desenvolvimento contínuo. Sugestões e contribuições são bem-vindas!

## ✨ Funcionalidades Principais

- Interação via Discord usando comando `/sarah`
- Bot do Telegram respondendo a mensagens diretas
- API REST para integração com outros sistemas
- Sistema de memória para manter contexto das conversas
- Personalidade consistente em todas as plataformas

## 🔐 Segurança

- Todas as chaves de API são armazenadas em variáveis de ambiente
- Validação de entrada em todas as interfaces
- Tratamento de erros robusto

## 📝 Notas

- O servidor web mantém o bot sempre online
- A Sarah utiliza o modelo meta-llama/llama-3-8b-instruct via OpenRouter
- As respostas são sempre em português do Brasil

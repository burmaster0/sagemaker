AWS has solved one of the biggest problems that most NLP data scientists face, ie How to Deploy HuggingFace LLM models as endpoints. The HuggingFace community hosts a huge list of Opensource LLM models that outperform ChatGPT in most of the use cases.

OpenAI and Google have restricted their LLM models and the only way we can access those is by making API calls to their servers with prompts. These APIs respond with the generated text and charge based on the input token size. These models, despite being restricted, provide very high-quality response and fast processing speeds. However, they also take away a lot of benefits as compared to the Open source LLM models.


There are many benefits when u deploy HuggingFace LLM models on AWS:

Control: You have more control over the architecture. For OpenAI LLM models we have to send our data to their endpoints to get the generated text.
Security: As we are sending the data to an external server, such as OpenAI, there is a risk of security issues.
Cost: It can be cheaper than using 3rd Party LLM services.
Deploy HuggingFace LLM as Endpoints – AWS
Now let’s look at how AWS has enabled deploying huggingface LLM models as endpoints. Currently, AWS has the following Officially supported model architectures:

BLOOM / BLOOMZ
MT0-XXL
Galactica
SantaCoder
GPT-Neox 20B (joi, pythia, lotus, rosey, chip, RedPajama, open assistant)
FLAN-T5-XXL (T5-11B)
Llama (vicuna, alpaca, koala)
Starcoder / SantaCoder
Falcon 7B / Falcon 40B
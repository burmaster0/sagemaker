import sagemaker
import json
from sagemaker.huggingface import HuggingFaceModel
# Define Model and Endpoint configuration parameter
hf_model_id = "OpenAssistant/pythia-12b-sft-v8-7k-steps" # model id from huggingface.co/models
# hf_model_id = "OpenAssistant/falcon-7b-sft-mix-2000" # model id from huggingface.co/models
use_quantization = False # wether to use quantization or not
instance_type = "ml.g5.12xlarge" # instance type to use for deployment
number_of_gpu = 4 # number of gpus to use for inference and tensor parallelism
health_check_timeout = 300 # Increase the timeout for the health check to 5 minutes for downloading the model
# create HuggingFaceModel with the image uri
llm_model = HuggingFaceModel(
  role=role,
  image_uri=llm_image,
  env={
    'HF_MODEL_ID': hf_model_id,
    'HF_MODEL_QUANTIZE': json.dumps(use_quantization),
    'SM_NUM_GPUS': json.dumps(number_of_gpu)
  }
) 

prompt=f"""<|prompter|write a poem on the beauty iran country.<|endoftext|><|assistant|>"""
# hyperparameters for llm
payload = {
  "inputs": prompt,
  "parameters": {
    "do_sample": True,
    "top_p": 0.7,
    "temperature": 0.7,
    "top_k": 50,
    "max_new_tokens": 512,
    "repetition_penalty": 1.03,
    "stop": ["<|endoftext|>"]
  }
}
# send request to endpoint
response = llm.predict(payload)
runtime = boto3.client('runtime.sagemaker')
response = runtime.invoke_endpoint(EndpointName = 'llm-endpoint',
                                        ContentType = 'application/json',
                                        Body = json.dumps(payload))
output = response['Body'].read().decode()
output_json = json.loads(output[1:-1])['generated_text'].split("<|assistant|>")[1]
print(output_json)
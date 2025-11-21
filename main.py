from vllm.entrypoints.openai.api_server import run_server
import os

run_server(
    model="Arynix/Arynix-70B-SpacePreview",   # your model on HF
    tensor_parallel_size=1,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)),
    allow_credentials=True,
    served_model_name="arynix"
)

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama-1.1B-Chat-v1.0",
    task='text_generation',
    pipeline_kwargs=dict(
        temprature=0.5,
        max_new_tokens =100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of india")
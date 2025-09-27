
import torch
from transformers import pipeline

print("Loading Hugging Face model... This may take a while.")

# 1. Create a text-generation pipeline
#    - device_map="auto" will automatically use your GPU if it's available.
#    - trust_remote_code=True is required for this model architecture.
pipe = pipeline(
    "text-generation",
    model="microsoft/Phi-3-mini-4k-instruct",
    device_map="auto",
    torch_dtype="auto",
    trust_remote_code=True,
)

def get_hf_answer(query, passages):
    """
    Generates an answer using a locally-hosted Hugging Face model.
    """
    normalized_query=query.strip().lower()
    simple_answers={"what is your name?":"I am your gst assistant,here to help you...",
                    "what is full form of gst":"GST stands for Goods and Services Tax. It is a unified indirect tax system in India.",
                    "types of gst":"There are four types of GST: CGST, SGST, IGST, and UTGST.",
                    "when was gst implemented":"GST was implemented in India on July 1, 2017."}
    if normalized_query in simple_answers:
        return simple_answers[normalized_query]


    # 2. Format the prompt correctly for the Phi-3 model
    #    Every model has a specific format it was trained on. This is crucial.
    context = " ".join(passages)
    prompt = f"""<|user|>
You are a helpful Indian GST assistant. Based ONLY on the following context, answer the user's question.

CONTEXT:
{context}

QUESTION: {query}<|end|>
<|assistant|>
"""

    try:
        # 3. Generate the response
        #    max_new_tokens controls the maximum length of the answer.
        #    eos_token_id is used to know when the model has finished generating.
        outputs = pipe(
            prompt,
            max_new_tokens=512,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            eos_token_id=pipe.tokenizer.eos_token_id,
        )

        # 4. Extract the generated text
        #    The answer is inside a nested structure. We need to parse it out.
        generated_text = outputs[0]['generated_text']
        
        # The model's output will include your original prompt, so we split it off.
        answer = generated_text.split("<|assistant|>")[1].strip()
        return answer

    except Exception as e:
        print(f"An error occurred with the Hugging Face model: {e}")
        return "Sorry, I encountered an issue while generating an answer with the local model."
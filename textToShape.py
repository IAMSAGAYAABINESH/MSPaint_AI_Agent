from prompt import PROMPT_TEMPLATE
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

chat_history = []

def generate_and_save_drawing(input_query, filename="drawShape.py"):
    print("Generating drawing-commands...")
    global chat_history
    
    client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY"),
    )
    model = "gemini-2.5-pro"
    
    contents = []
    
    if len(chat_history) == 0:
        system_prompt = PROMPT_TEMPLATE.replace("{input_query}", input_query)
        contents.append(types.Content(
            role="user",
            parts=[types.Part.from_text(text=system_prompt)]
        ))
    else:
        first_entry = chat_history[0]
        if "system_prompt" in first_entry:
            contents.append(types.Content(
                role="user",
                parts=[types.Part.from_text(text=first_entry["system_prompt"])]
            ))
        
        for entry in chat_history:
            contents.append(types.Content(
                role="user",
                parts=[types.Part.from_text(text=entry["input_query"])]
            ))
            contents.append(types.Content(
                role="model",
                parts=[types.Part.from_text(text=entry["generated_code"])]
            ))
        
        contents.append(types.Content(
            role="user",
            parts=[types.Part.from_text(text=input_query)]
        ))
    
    generate_content_config = types.GenerateContentConfig(
        temperature=0.6,
        top_p=0.95,
        max_output_tokens=12000,
    )
    
    completion = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )
    
    generated_code = completion.text
    
    if len(chat_history) == 0:
        chat_entry = {
            "input_query": input_query,
            "system_prompt": PROMPT_TEMPLATE.replace("{input_query}", input_query),
            "generated_code": generated_code
        }
    else:
        chat_entry = {
            "input_query": input_query,
            "generated_code": generated_code
        }
    
    chat_history.append(chat_entry)
    
    with open(filename, "w") as file:
        file.write(generated_code)
    
    return generated_code

def get_chat_history():
    return chat_history

def clear_chat_history():
    global chat_history
    chat_history = []
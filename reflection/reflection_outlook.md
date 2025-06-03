# Ausblick
Dieser Ausblick wird irgendwann eine Reproduktion der vorhergehenden Studie auf einem LLM-korrigierten Volltextkorpus präsentieren und diese Ergebnisse mit denen der Fallstudie vergleichen. 

Wir müssen allerdings erst einmal rausfinden, wie 1.321 txt-Dateien im Umfang von 166 MB durch ein LLM korrigieren lassen.

Wir haben schon mal ChatGPT gefragt. Das ergab dies


## Prompt
> Hello. You are an experienced digital engineer who specializes in working with the APIs of Large Language Models. Now you are faced with the following challenge. 
> 
> You have a folder with 1,321 txt files. The files in the folder are 166 megabytes in size. The largest file is 424 kilobytes in size and contains 416313 characters. 
> 
> The text in these files is now to be edited by accessing the GPT API. Texts were created from PDFs using OCR with pyTesseract. Each PDFs represents a German-language newspapers in Gothic font from the years 1918 and 1919. Since pyTesseract has some problems with this type of font, the quality of the OCR output is suboptimal. API access to GPT should significantly improve the quality by correcting the text. 
> 
> How do you proceed now? Please describe the solution. Please also provide the terminal commands that you will execute on you Mac computer. Please also note any limitations of the GPT API, both in terms of the length or size of the files (input and output) and with regard to limits for API calls. 
> 
> As additional information: You have a ChatGPT Plus subscription.
> 

## Output
To tackle this challenge, follow these steps:

1.	Break Down the Text Files: Given the size limitations of the GPT API, you’ll need to split the text files into smaller chunks. The GPT-4 API (including ChatGPT) typically handles input text up to a few thousand tokens per request. For safety, assume a maximum of around 4096 tokens (about 3000 words) per request.
2.	Script to Split Files: Write a Python script to read the files, split them into manageable chunks, and send each chunk to the GPT API for correction.
3.	Edit the Text: Use the OpenAI GPT API to process each chunk. The API will return the corrected text, which you’ll need to save back to a file.
4.	Reassemble Files: After all chunks are processed, reassemble them into the original files.
5.	API Rate Limits: Be aware of the API’s rate limits. With a ChatGPT Plus subscription, the rate limits are higher than the free tier, but you still need to manage requests efficiently.

Here’s a step-by-step guide with terminal commands and a Python script:

**Step 1: Prepare Your Environment**
Open your terminal and ensure you have Python and necessary packages installed:

```
# Install necessary Python packages
pip install openai tqdm
```

**Step 2: Python Script to Process Files**
Create a Python script, process_files.py, with the following content:

```
import os
import openai
from tqdm import tqdm

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key'

# Directory containing the text files
input_dir = 'path_to_your_folder'
output_dir = 'path_to_output_folder'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to split text into chunks
def split_text(text, max_tokens=3000):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        current_length += len(word) + 1  # +1 for space
        if current_length > max_tokens:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = len(word) + 1
        current_chunk.append(word)
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks

# Function to process text with GPT API
def correct_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Correct the OCR errors in the following German text."},
            {"role": "user", "content": text}
        ]
    )
    return response['choices'][0]['message']['content']

# Process each file
for filename in tqdm(os.listdir(input_dir)):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_dir, filename)
        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        chunks = split_text(text)
        corrected_text = []

        for chunk in chunks:
            corrected_chunk = correct_text(chunk)
            corrected_text.append(corrected_chunk)

        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(' '.join(corrected_text))
```

**Step 3: Run the Script**
In your terminal, navigate to the directory where process_files.py is located and run it:

```
python process_files.py
```

**Limitations and Considerations**

1.	Token Limit: The GPT-4 API has a token limit per request (4096 tokens for input and output combined). Ensure each chunk you send does not exceed this limit.
2.	Rate Limits: The API has rate limits on the number of requests per minute. With a ChatGPT Plus subscription, these limits are higher, but you should still monitor and respect them. Consider implementing rate limiting in your script if necessary.
3.	Cost: Be aware of the API usage costs, as processing large amounts of text can be expensive.

By following these steps, you can efficiently process and correct your OCR-generated text files using the GPT API.
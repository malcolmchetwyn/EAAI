import openai
import base64
from PIL import Image
from io import BytesIO
import os
import aiohttp
import asyncio
import json
import pprint 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


openai.api_key = OPENAI_API_KEY

async def get_image_analysis(image_path):
    # Read and encode the image
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    base64_encoded_image = base64.b64encode(image_bytes).decode('utf-8')

    # Decode the base64 string and open image
    image_bytes = base64.b64decode(base64_encoded_image)
    image = Image.open(BytesIO(image_bytes))

    # Resize the image to 512x512
    resized_image = image.resize((512, 512))

    # If you want to re-encode to base64
    buffered = BytesIO()
    resized_image.save(buffered, format=image.format)
    resized_base64 = base64.b64encode(buffered.getvalue()).decode()

    dir_path = "."

    prompt = "describe this "

# Read the patterns and guardrails content
    with open('DataIntegrationDecisonGuidelines.html', 'r') as file:
        well_architectured_data_integration_guidelines= file.read()
    with open('DesignPatternsWithProduct.rtf', 'r') as file:
        well_architectured_design_patterns= file.read()
    with open('ootb.rtf', 'r') as file:
        salesforceOOTBs= file.read()

    with open('CustomerGR.txt', 'r') as file:
        CustomerGR= file.read()

    prompt = f"""f

    
        BASED ON THE ARCHITECTURE DIAGRAM PASSED IN AND USING THE CONFIDENCE INDEX RATING. 
        ASSESS THE CONFIDENCE LEVEL OF THE ARCHITECTURE MODEL AND HOW IT ALIGNS TO THE WELL ARCHITECTED GUIDELINES AND WELL ARCHITECTED DESIGN PATTERNS AND CUSTOMER GUARDRAILS

        WELL ARCHITECTED GUIDELINES
        {well_architectured_data_integration_guidelines}

        WELL ARCHITECTED DESIGN PATTERNS
        {well_architectured_design_patterns}

        OOTB PATTERNS
        {salesforceOOTBs}

        GIVE JUST ONE CONFIDENCE INDEX NUMBER

        WHAT IS THE RECOMMENDED INTEGRATION METHOD

        IF THIS IS IMPLEMENTED IN SALESFORCE WHAT OUT OF THE BOX CAPABILITIES COULD BE LEVERAGED USING OOTB PATTERNS AS INPUT

        Confidence Index broken up by value and dewscripiton 
        10, Excellent, The response is perfect. It is highly accurate, complete, relevant, and exceptionally well-articulated. No improvements are needed.
        9, Very Good, The response is nearly perfect. It is highly accurate and relevant but might lack a minor detail or have a slight improvement in articulation.
        8, Good, The response is accurate and relevant but might miss a couple of minor details or have minor issues in articulation.
        7, Fairly Good, The response is mostly accurate and relevant but might miss a few details or have some issues in articulation.
        6, Satisfactory, The response is generally accurate but lacks several details or has notable issues in articulation. It still provides value.
        5, Average, The response is somewhat accurate but misses several key details or has significant issues in articulation. It provides some value but needs improvement.
        4, Below Average, The response is partially accurate but misses many key details and has major issues in articulation. It provides limited value.
        3, Poor, The response is largely inaccurate or irrelevant with substantial missing details and severe issues in articulation. It provides minimal value.
        2, Very Poor, The response is highly inaccurate or irrelevant with almost all key details missing and major articulation issues. It provides very little value.
        1, Terrible, The response is almost entirely inaccurate or irrelevant with no useful details and extremely poor articulation. It provides negligible value.
        0, Untrustworthy, The response is completely inaccurate or irrelevant with no useful information and is misleading or deceptive. It provides no value and cannot be trusted.




        
        """


    # Ensure the directory exists
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    filename = os.path.basename(image_path)
    filepath = os.path.join(dir_path, filename)

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{resized_base64}",
                            "detail": "high"  # This is how you specify the image quality detail
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload) as response:
            if response.status == 200:
                response_data = await response.json()
                description = response_data['choices'][0]['message']['content']
                return {"description": description}
            else:
                response_text = await response.text()
                raise Exception(f"Error from OpenAI: {response_text}")

# Example usage
# image_path = 'arch_model.png'
image_path = 'WellATest.png'
# image_path = 'IBM.png'
# image_path = 'SFRetailBanking.png'
response = asyncio.run(get_image_analysis(image_path))
pprint.pprint(response, width=150)
# print(response)

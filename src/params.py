import os

settings = {
    "dsg": {
        "openai_api_key": os.getenv("OPENAI_API_KEY"),
        "gemini_api_key": os.getenv("GEMINI_API_KEY"),
        "llama_api_key": os.getenv("LLAMA_API_KEY"),
        "output_dir": "./dsg/data/",
        "sys_prompt_identify": "", # Will be used in the future to classify explicit/implicit aspect containing reviews
        "user_prompt_identify": "",
        "sys_prompt_label": """
            You are a data annotator working in the field of review analysis.
            In reviews, customers have a sentiment (positive, neutral, or negative) towards aspects of a product or service.
            You will be given reviews with aspects, where the term may or may not be mentioned explicitly in the text. You are tasked to generate a fitting aspect term.

            You are to output a single word (term) that fits what you judge to be the aspect of the product or service that the review is directing its sentiment towards.
            Do not output any other text aside from the term alone as the system requires the format to be in this output.

            Some examples of potential inputs and outputs:

            Input: Given the review "The quality is not nearly good enough for video calls", in the category laptop, where the sentiment is negative, generate a fitting aspect term.
            Output: webcam

            Input: Given the review "Had to ask him 3 time before he finally corrected my order", in the category restaurant, where the sentiment is negative, generate a fitting aspect term.
            Output: service

            Input: Given the review "It holds a charge for so long", in the category phone, where the sentiment is positive, generate a fitting aspect term.
            Output: battery
        """,
        "user_prompt_label": "Given the review \"%s\", in the category %s, where the sentiment is %s, generate a fitting aspect term.",
        "path": "../data/raw/semeval/toy.2016SB5/ABSA16_Restaurants_Train_SB1_v2.xml", # Last 3 params altered dynamically at runtime
        "category": "restaurant",
        "model": "gpt-4o-mini",
        "eval": {
            "embedding_model": "text-embedding-3-small", # For evaluating models against ground truth
            "similarity_threshold": 0.5,
        }
    }
}
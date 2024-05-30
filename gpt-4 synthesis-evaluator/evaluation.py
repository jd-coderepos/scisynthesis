# -*- coding: utf-8 -*-
import openai
import pandas as pd
import time


# Configuration
CONFIG = {
    'SYNTHESIS_TYPE': '', # paper-wise, methodological, or thematic
    'SYSTEM_PROMPT_FILE': '', # path to file
    'SYNTHESIS_FILE': '', # path to file
    'OUT_FILE': '', # file name for saving output in .xlsx
    'OPENAI_API_KEY': '',
    'API_MODEL': 'gpt-4-1106-preview',
    'RESPONSE_FORMAT': 'json_object',
    'API_TEMPERATURE': 0,
    'MAX_TOKENS': 700,
    'API_STOP_SEQUENCE': '###',
    'API_CALL_DELAY': 10  # seconds
}


def build_prompt(row):
    """
    Build the user prompt for the API call.
    """
    user_prompt_text = 'Evaluate and rate the quality of the following scientific synthesis according to the nine characteristics given in the system prompt.'
    content = format_paper_content(row).strip()
    problem = row['research_problem']
    synthesis = row['synthesis_text']
    return (
        f'{user_prompt_text}\n\n'
        f'<scientific-synthesis>{synthesis}</scientific-synthesis>\n\n'
        f'<research-problem>{problem}</research-problem>\n\n'
        f"<synthesis-type>{CONFIG['SYNTHESIS_TYPE']}</synthesis-type>\n\n"
        f'<paper-titles-and-abstracts>{content}</paper-titles-and-abstracts>\n\n###'
    )


def format_paper_content(row):
    """
    Format the paper titles and abstracts for each sample (row).
    """
    paper_content = ''
    for i in range(5):
        title = row[f'paper_{i+1}_title']
        abstract = row[f'paper_{i+1}_abstract']
        paper_content += f'{i+1}. ' + title + '\n\n' + abstract + '\n\n'
    return paper_content


def call_gpt4_api(message):
    """
    Call the GPT-4 API with the given message
    """
    return openai.ChatCompletion.create(
        model = CONFIG['API_MODEL'],
        response_format = CONFIG['RESPONSE_FORMAT'],
        messages = message,
        temperature = CONFIG['API_TEMPERATURE'],
        max_tokens = CONFIG['MAX_TOKENS'],
        stop = [CONFIG['API_STOP_SEQUENCE']]
    )       
    

def main():
    """
    Main function to evaluate scientific syntheses using the OpenAI GPT-4 API.

    This function performs the following steps:
    
    1. Loads the system prompt from a specified file.
    2. Reads a synthesis file (.xlsx) containing syntheses, research problems, and paper details.
    3. Iterates over each row in the synthesis file to build a prompt for the GPT-4 API.
    4. Calls the GPT-4 API with the generated prompt and captures the response.
    5. Handles any exceptions that occur during the API call and logs them.
    6. Inserts the API response (evaluation) into the corresponding row in the DataFrame.
    7. Pauses between API calls to avoid rate limit issues.
    8. Saves the updated DataFrame with the evaluations to a new Excel file.

    Configuration values such as file paths, API key, and model parameters are specified in the CONFIG dictionary.
    """
    # assign API key
    openai.api_key = CONFIG['OPENAI_API_KEY']

    # load system prompt
    with open(CONFIG['SYSTEM_PROMPT_FILE'], 'r') as f:
        system_prompt = f.read()

    # read synthesis file into dataframe and add column for evaluation output
    df = pd.read_excel(CONFIG['SYNTHESIS_FILE'])
    df.insert(df.shape[1], 'gpt_evaluation', '')

    # call API for each sample in data
    for index, row in df.iterrows():
        user_prompt = build_prompt(row)
        message = [{"role": "system", "content": system_prompt},
                   {"role": "user", "content": user_prompt}]


        # try to call the API
        try:
            response = call_gpt4_api(message)
            df.at[index, 'gpt_evaluation'] = response
            
        # catch and record in case of exception
        except Exception as error:
            df.at[index, 'gpt_evaluation'] = f"Unexpected {error}, {type(error)}"
    
        # pause to avoid RateLimitError
        time.sleep(CONFIG['API_CALL_DELAY'])

    df.to_excel(CONFIG['OUT_FILE'], index=False)

main()

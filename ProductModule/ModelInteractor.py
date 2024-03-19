import openai

class ModelInteractor:

    def __init__(self, api_key, api_type, api_base, api_version, engine):
        openai.api_key = api_key
        openai.api_type = api_type
        openai.api_base = api_base
        openai.api_version = api_version
    
    def wrap_code_in_docstring(code):
        return f'"""\n{code}\n"""'

    def generate_prompt(self, code_content):
        code_to_process = ModelInteractor.wrap_code_in_docstring(code_content)
        #.md prompt
        prompt = f"""
                Given a code snippet enclosed in triple backticks: 
                ```{code_to_process}``` 
                You a tasked to perform the below operations
                
                1) Identify the programming language
                2) refactor as per the programming language contraints such as variable, function, class names etc..
                2) Write clear & explainable documentation as per identifed language offical docs
                3) Explain the code with clear & proper comments, such as line by line explaination
                3) summarize the functionality at the end
                
                Perform all the operations & generate a response in format of .md file, the title, headings to be described as per the crips functionality of code
                """
        # .html prompt
        # prompt = f"""

        # Given a code snippet enclosed in triple backticks: 
        #        ```{code_to_process}``` 
        #     Identify the programming language based on the file extension. Perform the following tasks:

        #     1. Determine the programming language.
        #     2. Process the content of the file accordingly.
        #     3. Generate human-readable code documentation or response.

        #    Perform all the operations & generate a response in format of .html file, the title, headings to be described as per the crips functionality of code with proper styling & alignments
        #     """

        #.txt prompt
        # prompt = f"""

        # Given a code snippet enclosed in triple backticks: 
        #        ```{code_to_process}``` 
        #     Identify the programming language based on the file extension. Perform the following tasks:

        #     1. Determine the programming language.
        #     2. Process the content of the file accordingly.
        #     3. Generate human-readable code documentation or response.

         #   Perform all the operations & generate a response in format of .txt file, with proper alignment & spacing
        #     """
        message_text = [
            {"role": "system", "content": "You are a Coding AI assistant that helps write clear, human-readable documentation following the official programming language documentation style."},
            {"role":"user", "content": prompt }
            ]
        
        return message_text

    def collect_model_response(self, prompt, engine):
        
        try:
            print("Processing your code....")
            response = openai.ChatCompletion.create(
                    engine=engine,
                    messages = prompt,
                    temperature=0.7,
                    max_tokens=800,
                    top_p=0.95,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=None
                )
            print("response ", response.choices[0].message.content)
            return response.choices[0].message.content
        except openai.error.APIError as e:
            print(f"APIError: {e}")
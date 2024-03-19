from CodeLoader import CodeLoader
from ModelInteractor import ModelInteractor
from ResultFormatter import ResultFormatter
import os
from dotenv import load_dotenv
load_dotenv()

class CodeUnderstandingApp:

    def __init__(self, api_key, api_type, api_base, api_version, engine) -> None:
        self.loader = CodeLoader()
        self.model_interactor = ModelInteractor(api_key, api_type, api_base, api_version, engine)
        self.formatter = ResultFormatter()
    
    def run(self, code_file_path, output_file_path, engine):
        code_content = self.loader.load_code_file(code_file_path)
        prompt = self.model_interactor.generate_prompt(code_content)
        model_response = self.model_interactor.collect_model_response(prompt, engine)
        self.formatter.format_and_save_result(code_content, model_response, output_file_path)

if __name__ == "__main__":
    
    
    
    api_key = 'api_key'
    api_type = 'azure'    
    api_base = 'api_base'
    api_version = '2023-07-01-preview'
    engine = 'engine'
    
    code_file_path = "C:\dev-workspace\Hackathon\Open-API-Spec\pythonProject\Gen-AI-Projects\FineTunningModel\input_files\Solution.java"
    output_file_path = "C:\dev-workspace\Hackathon\Open-API-Spec\pythonProject\Gen-AI-Projects\FineTunningModel\output_files\output.md"

    
    # Create and run the CodeUnderstandingApp
    app = CodeUnderstandingApp(api_key=api_key, api_type=api_type, api_base=api_base, api_version=api_version, engine=engine)
    app.run(code_file_path=code_file_path, output_file_path=output_file_path, engine=engine)

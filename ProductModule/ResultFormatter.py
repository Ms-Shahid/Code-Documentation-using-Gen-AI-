
from IPython.display import display, HTML
class ResultFormatter:
    @staticmethod
    def format_and_save_result(code_content, model_response, output_file_path):
        #formatted_result = "Original Code:\n{}\n\nModel Response:\n{}".format(code_content, model_response)
        with open(output_file_path, 'w') as output_file:
            output_file.write(model_response)

# class ResultFormatter:
#     @staticmethod
#     def format_and_save_result(code_content, model_response, output_file_path):
#         with open(output_file_path, 'w') as output_file:
#             output_file.write(model_response)
        
#         # Read the content from the generated file
#         with open(output_file_path, 'r') as output_file:
#             html_content = output_file.read()

#         # Display the HTML content
#         display(HTML(html_content))



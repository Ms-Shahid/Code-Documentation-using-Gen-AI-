class CodeLoader:
    @staticmethod
    def load_code_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except Exception as e:
            print("Unable to process the file:", e)
            return None




import inspect


def run(app):
    if inspect.ismodule(app):
        exec(app)
    else:
        error("pass a module to be run")

class MyApp:
    def __init__(self, *args):
        for arg in args:
            setattr(self, arg, None)
        
    def __call__(self):
        # Check if all variables are set
        for attr in self.__dict__:
            if getattr(self, attr) is None:
                raise ValueError(f"{attr} is not set")
        
        # Run the benchmarking
        dataset = load_dataset(self.file_path)
        results = run_benchmark(dataset, self.questions)
        save_results(results)
        
    def setup(self):
        # Get values for all variables dynamically
        for attr in self.__dict__:
            if getattr(self, attr) is None:
                print(f"Please enter the value for {attr}:")
                value = input().strip()
                setattr(self, attr, value)


class MyApp:
    def __init__(self):
        self.file_path = None
        self.questions = None
        
    def __call__(self):
        if self.file_path is None:
            raise ValueError("Dataset file path is not set")
        if self.questions is None:
            raise ValueError("Questions list is not set")
        
        # Run the benchmarking
        dataset = load_dataset(self.file_path)
        results = run_benchmark(dataset, self.questions)
        save_results(results)
        
    def setup(self):
        # Define guidance methods for loading the dataset file
        print("Please enter the path to the dataset file:")
        self.file_path = input().strip()
        
        # Define guidance methods for loading the questions
        self.questions = []
        print("Please enter the benchmarking questions (press enter to finish):")
        while True:
            question = input().strip()
            if question == "":
                break
            self.questions.append(question)


class AnonymousSurvey:
    def __init__(self,question):
        """Store a question and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)
        
    def store_response(self, new_reponse):
        """Store a single reponse to the survey."""
        self.responses.append(new_reponse)
        
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
        
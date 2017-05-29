class AnonymousSurvey():
    """collect anonymous survey answers"""

    def __init__(self,question):
        """Store a question, and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show survey question"""
        print(self.question)

    def store_response(self,new_response):
        """store single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all the responses that have been given"""
        print("Survey results: ")
        for response in self.responses:
            print('-'+response)

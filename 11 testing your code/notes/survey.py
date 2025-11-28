##testing a class##

#writing tests for classes
#proves they work correctly
#if tests pass on a class you work on, you can be confident improvements you make
#to that class wont accidently break its current behaviour

#when writing a test, you can make any claim that can expressed as a conditional statement
#if the condition is true as ecpected, your assumption about how that part of your
#program behaves will be confirmed; you can be confident that no errors exist

#commonly used assertion statements in test
#asserion/claim:
#assert a == b //assert that two values are equal
#assert a !=b //assert that two values are not equal
#assert a //assert that a evaluates to true
#assert not a //assert that a evalutes to false
#assert element in list //assrt that an element is in a list
#assert element not in list //assert that element is not in a list

#few examples from book

#class to test

class AnonoymousSurvey:
    "collect anonymous answers to a survey question"
    
    def __init__(self,question):
        """store question and its responses"""
        self.question = question
        self.responses = []
        
    def showquestion(self):
        """show the survey question"""
        print(self.question)
        
    def store_response(self, new_response):
        """store a single response to the survey"""
        self.responses.append(new_response)
        
    def show_results(self):
        """show all responses that are given"""
        print("survey results:")
        for response in self.responses:
            print(f"- {response}")
            


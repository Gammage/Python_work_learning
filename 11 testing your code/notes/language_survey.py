from survey import AnonoymousSurvey

#define a question, and make a survey:
question = "what language did you first learn to speak?"
language_survey = AnonoymousSurvey(question)

#show the question, and store responses to the question
language_survey.showquestion()
print("enter q at any time to quit\n")

while True:
    response = input('language:')
    if response == 'q':
        break
    language_survey.storeresponse(response)
    
#show results
print("\nThank you to everyone who participiated in the survey")
language_survey.show_results()
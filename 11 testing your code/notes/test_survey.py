from survey import AnonoymousSurvey

@pytest.fixture
def language_survey():
    """a survey that will be available to all test functions"""
    question = "what language did you first learn to speak?"
    language_survey = AnonoymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """test that a single response stored correctly"""
    language_survey.store_response('english')
    assert 'english' in language_survey.responses
    
def test_store_three_respones(language_survey):
    """test that multuple responses are stored correctly"""
    responses = ['english','french','spanish']
    for response in responses:
        language_survey.store_response(response)
        
    for response in responses:
        assert response in language_survey.responses

#using fixtures#
#we created a new instance of anonymous survey in each test function
#in a real project with lots of tests this would be problematic
#a fixture helps set up a testing environment
#this means creating a resource thats used by more than one test
#we create a fixture in pytest by writing a function with the decorator @pytest.fixture
#a decorator is a directive placed just before a function definition;
    #python applies this directive to the function before it runs, to alter how the
    #function code behaves.
    #it sounds fucking complicated, you can use decorators from third-party packages
    #before learning to write them yourself
    #see above fixtures in code
    
#fixtures can be complicated, better to add repetitive code to define test use cases
#and eventually use fixtures rather than write no tests at all

#examples of testing above makes little sense with small amounts of code but makes 
#sense with larger code to test

#when you want to write a fixture, write a function that generates the resource
#used by multiple test functions, add the @pytest.fixture decorator to the new function
#add the name of this function as a parameter for each test function that uses this resource
#tests will be shorter and easier to write and maintain from that point forward
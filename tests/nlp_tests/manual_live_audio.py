# WARNING! RUN THE TEST WITH THE "-s" FLAG IN ORDER TO 
# PROPERLY RUN
# example: pytest -s tests/nlp_tests/manual_live_audio.py

from nlp.speech_to_text import stt
import pyaudio

# Defining the sentences to be used in the test
sentences = {}
sentences[0] = "the cat sat on the window sill watching the birds outside"
sentences[1] = "this is a test of a longer sentence"
sentences[2] = "the meeting has been rescheduled for next Thursday"
sentences[3] = "she enjoys reading books about ancient history"
sentences[4] = "the sunset painted the sky with shades of orange and pink"
sentences[5] = "can you help me find the nearest coffee shop"

# Function to read the sentence and compare it to the spoken sentence
def reader(i):
    print("")
    print("\033[1mTest \033[0m" + str(i+1) + ":")
    print("\033[1mSay the following sentence: \033[0m")
    print(sentences[i])
    print("")
    print("Press enter to start recording...")

    input()
    speech = stt()

    if(speech == sentences[i]):
        print("You said: " + speech)
        print("Test " + str(i+1) + " passed")
        assert True
    else:
        print("You said: " + speech)
        print("Test " + str(i+1) + " failed")
        assert False

# Running the tests
print("")
print("")
print("Enter the number of tests you would like to run (1-5): ")
num_tests = int(input())
for i in range(num_tests):
    reader(i)




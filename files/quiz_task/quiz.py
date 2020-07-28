"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""


quiz_questions = open('questions.txt', 'r')
sample = [line.strip() for line in quiz_questions.readlines()]
dict_of_answers = dict([string.split('=') for string in sample])
quiz_questions.close()

number_of_questions = len(dict_of_answers)
score = 0

for k,v in dict_of_answers.items():
    user_answer = input(f'What is your answer to {k} ? ')
    if user_answer == v:
        score +=1

result = open('result.txt', 'w')
result.write(f'Your final score is {score}/{number_of_questions}.')
result.close()

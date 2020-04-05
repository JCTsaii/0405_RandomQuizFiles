'''
35 students, 50 Questions
1. random module
2. generate 35 quizFiles
3. 50 Question and Ans (correct answer\ wrong answer (random ABCD))                 
'''
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for quizFilesNum in range(35):
    quizFile=open('quizFile{}'.format(quizFilesNum+1),'w')
    quizFile.write('Name:    Date:    QuizForm {}\n\n'.format(quizFilesNum+1))
    ansFile=open('ansFile{}'.format(quizFilesNum+1),'w')
    ansFile.write('Answer for QuizForm {}\n\n'.format(quizFilesNum+1))
    states=list(capitals.keys())
    random.shuffle(states)
    for quizNum in range(50):
        correctAns=capitals[states[quizNum]]
        wrongAns=list(capitals.values())
        del wrongAns[wrongAns.index(correctAns)]
        wrongAns=random.sample(wrongAns,3)
        ansOpt=wrongAns+[correctAns]
        random.shuffle(ansOpt)
        quizFile.write('{}. What is the capital of {}?\n'.format((quizNum+1),states[quizNum]))
        
        for i in range(4):
            quizFile.write('ABCD'[i]+'. {}\n'.format(ansOpt[i]))
        quizFile.write('\n')
    
        ansFile.write('{}. {} \n'.format((quizNum+1),'ABCD'[ansOpt.index(correctAns)]))
    quizFile.close()
    ansFile.close()




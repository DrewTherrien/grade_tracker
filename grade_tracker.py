names=[]
scores=[]

print('=== Student Grade Tracker ===')
print('Enter student names and scores. Type done when finished.')

name=input('Enter student name (or done to stop): ')

while name != 'done':
    score= int(input('Enter score for ' + name + ':'))
    
    if score < 0 or score > 100:
        print('Score must be between 0 and 100. Try again.')
    else:
        names.append(name)
        scores.append(score)
        print(name + 'added!')
    name= input('Enter student name (or done to stop): ')
print('Data entry complete. ' + str(len(names)) + ' students entered.')
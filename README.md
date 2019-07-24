# Code-2019
### Program 1: Seating arrangements
A School is hosting its annual day function and has invited all of its students to be accompanied with their parents. Now Mrs.Suzane who is in charge of the event has to get the seating order right so that everyone could watch the events without any hinderances. The arrangements has to be in such a way that each seat can “see” the front stage. A person can "see" the front-stage if they are strictly taller than the person sitting before them..
So help Mrs.Suzane by checking whether her arrangement is correct or not.
Consider every person’s height as a number.
A number can "see" the front-stage if it is strictly greater than the number before it.
Sample –
$FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],	Success
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]


#FRONT STAGE
[[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 	Failed
[5, 5, 5, 10, 4, 4], 
[6, 6, 7, 6, 5, 5]]

The function should return True if every number can see the front-stage, and False if even a single number cannot.

### Program 2: Vowel Position
In English language vowels plays an important role. a, e, i, o, u  are the vowel characters. Mia is learning vowels in her class this term. Her teacher has come up with a new way of teaching the vowels. 
To make the students recognize the vowels she has given them a task. Each student has been given a word containing at least one vowel character. From that word, Mia has to find out the shortest distance between each non vowel character and the vowel character. She was further told that if the character is a vowel itself then the distance is to be zero.
Note: The String is to be taken in kower case only
Sample –
Enter the String - abcdabcd
[0, 1, 2, 1, 0, 1, 2, 3]
Enter the String - shopper
[2, 1, 0, 1, 1, 0, 1]

### Program 3: Phone Numbers Repetition
given a list of phone numbers,no number is a prefix of another 
n is number of phone numbers

first line of input is n 1<=n<=10
following are the numbers taken as input 
input:
3
911
8452179965
9116565656
output:
No,there is a collision with 911

example2
input:
4
523
5245132
5278945
5277893
output:
Yes,it is consistent for 4 numbers

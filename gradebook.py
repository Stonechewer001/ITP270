 1 subjects = ["physics","calculus","poetry","history"]
 2 grades = [98,97,85,88]
 3 gradebook = [list(a) for a in zip(subjects, grades)]
 4                        
 5 print (gradebook)
 6 #5
 7 gradebook.append(["computer science",100])
 8 #6
 9 gradebook.append(["visual arts",93])
10 #7
11 gradebook[5] = (["visual arts",93 + 5])
12 #8
13 # practices using poetry_score = gradebook[2][1]
14 gradebook[2].remove(85)
15 #9
16 gradebook[2].append("Pass")
17 #10
18 #I made last semester the same as current semester
19 last_semester_gradebook = gradebook
20 print("_"*50)
21 full_gradebook = last_semester_gradebook + gradebook
22 print (full_gradebook)
23 

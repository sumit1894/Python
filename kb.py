questions=[
    ["1. Who developed Python Programming Language?"," Wick van Rossum"," Rasmus Lerdorf"," Guido van Rossum"," Niene Stom",3],
    
    ["2. Which type of Programming does Python support?" , "object-oriented programming", "structured programming", "functional programming", "all of the mentioned", 4],
    
    ["3.Is Python case sensitive when dealing with identifiers?" , "no", "yes", "machine dependent", "none of the mentioned", 2],
    
    ["4. Which of the following is the correct extension of the Python file?" , "python", ".pl", ".py", ".p", 3],
    
    ["5. Is Python code compiled or interpreted?" , "Python code is both compiled and interpreted", "Python code is neither compiled nor interpretedva", "Python code is only compiled", "Python code is only interpreted",  1],
    
    ["6. All keywords in Python are in _________" , "Capitalized", " lower case", "UPPER CASE", "None of the mentioned", 4],
    
    ["7. What will be the value of the following Python expression?- 4 + 3 % 5" , "7", "2", "4", "1", 1],
    
    ["8. Which of the following is used to define a block of code in Python language?" , " Indentation", "Key", "Brackets", " All of the mentioned", "none", 1],
    
    
    ["9. Which keyword is used for function in Python language?" , "Function", "def", "Fun", "Define", "Define", 2],
    
    ["10. Which of the following character is used to give single-line comments in Python??" , "//", " #", " !", "/*", "none", 2],
    
    ["11. Which of the following functions can help us to find the version of python that we are currently working on?" , "sys.version(1)", "sys.version(0)", " sys.version()", "sys.version", "none", 4],
    
    
    ["12. Python supports the creation of anonymous functions at runtime, using a construct called __________" , "pi", "anonymous", "lambda", " none of the mentioned", "none", 3],
    
    ["13. What is the order of precedence in python?" , "Exponential, Parentheses, Multiplication, Division, Addition, Subtraction", "Exponential, Parentheses, Division, Multiplication, Addition, Subtraction", " Parentheses, Exponential, Multiplication, Division, Subtraction, Addition", "Parentheses, Exponential, Multiplication, Division, Addition, Subtraction", 4],
    
    ["14. Which of the following is not a core data type in Python programming?" , "Tuples", "Lists", "Class", "Dictionary", "none", 3]
    
]
que=[
    ["1. Who developed Python Programming Language?"],
    ["2. Which type of Programming does Python support?"],
    ["3.Is Python case sensitive when dealing with identifiers?"],
    ["4. Which of the following is the correct extension of the Python file?"],
    ["5. Is Python code compiled or interpreted?"],
    ["6. All keywords in Python are in _________"],
    ["7. What will be the value of the following Python expression?- 4 + 3 % 5"],
    ["8. Which of the following is used to define a block of code in Python language?"],
    ["9. Which keyword is used for function in Python language?"],
    ["10. Which of the following character is used to give single-line comments in Python??"],
    ["11. Which of the following functions can help us to find the version of python that we are currently working on?"],
    ["12. Python supports the creation of anonymous functions at runtime, using a construct called __________"],
    ["13. What is the order of precedence in python?"],
    ["14. Which of the following is not a core data type in Python programming?"]
]
levels=[10000,20000,40000,80000, 1600000,320000,640000,125000,250000,500000,10000000,30000000,70000000]
money=0


for i in range(0,len(questions)):

    print(f"question for Rs. {levels[i]}")# levels work as loop
    print(que[i])
    question=questions[i]  # question will work in loop
    print(f"1. {question[1]}       2.{question[2]}")     
    print(f"3. {question[3]}       4.{question[4]}")   
     
    reply=int(input("Enter your answer(1-4)or 0 to quit\n:- "))
    print("\n") 
    if(reply==0):
        money=levels[i-1]
        break
    if(reply == question[-1]):
        print(f"correct answer, you have won Rs. {levels[i]}")
        print("\n")
        if(i==1):
            money=10000
        elif(i==6):
            money=320000
        elif(i==11):
            money=10000000
        
    else:
        print("wrong answer!")
        break
print(f"you have won Rs. {money}")






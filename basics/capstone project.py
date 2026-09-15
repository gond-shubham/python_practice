# capstone project ( Student Marks Analyzer )

N = int(input('enter the number of students.'))
std_names =[]
std_marks =[]
list_pass = []
list_fail = []


for i in range(N):
    name=input('enter the name:')
    std_names.append(name)
    mark = input('enter the marks')
    A = list(map(int, mark.split()[:5]))
    std_marks.append[A]
    m = min(A)
      for j in range(len(A)):
         if m<35:
             list_fail.append(name)
         else:
             list_pass.append(name)
    
            
    
             
            

        

        
              
          







    

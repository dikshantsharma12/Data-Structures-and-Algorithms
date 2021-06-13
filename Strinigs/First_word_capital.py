n = int(input("Enter number of elements : "))
  

input_list = list(map(str,input().strip().split()))[:n]
output_list=[]
for word in input_list:
    first_word=word[0].upper()
    last_word=""
    for char in range(1,len(word)):
       last=word[char].lower()
       last_word=last_word+last
    string=first_word+last_word
    output_list.append(string)
print(output_list)
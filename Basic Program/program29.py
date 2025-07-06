# def check_for_word():
#     word = "learning"
#     with open("sample.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
    
#         else:
#             print("Not found")
def check_for_line():
    word = str(input("Enter the word: "))
    data = True
    line_no = 1
    with open("sample.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1


    return -1
check_for_line()
            
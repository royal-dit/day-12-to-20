# #The quiz project
#
# class User:
#
#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username
#         self.follower = 0
#         self.following = 0
#         # print("New user beigng created")
#
#     def follow(self,user):
#         user.follower += 1
#         self.following += 1
#
#
# user_1 = User("001","angela")
# print(user_1.follower,user_1.id,user_1.username)
# print(user_1.follower)
# print(user_1.following)


# user_1.id = "001"
# user_1.username = "angela"



# user_2 = User()
# user_2.id= "001"
# user_2.name = "jack"


#
# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]
#
# # this will ask ,check the ans was right and end the game
# class QuizBrain:
#     def __init__(self,q_list):
#         self.question_number = 0
#         self.question_list = q_list
#
#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         input(f"Q.{self.question_number}:{current_question} (True/False)")
#
#
# class Question:
#     def __init__(self,q_text,q_answer):
#         self.text = q_text
#         self.answer=q_answer
#
# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text,question_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
# quiz.next_question()





class Emloyee:
    def printdetails(self):
        return (f"the name is {self.name} adress is {self.adress} and number is {self.no}")
royal = Emloyee()
royal.name = "Royal"
royal.adress = "jhumka"
royal.no = "9800947808"

print(royal.printdetails())



import foobar
import csv
from math import sqrt


class ChildClass(foobar.FoobarClass):

    def __init__(self, file_read):
        self.students = []
        self.emails = []
        self.card_labels = []
        self.scores = []
        self.file_read = file_read
        self.name = "ChildFoo"
        self.code_map = {'A1': 'a', 'A2': 'b', 'A3': 'c', 'A4': 'd', 'A5': 'e', 'A6': 'f', 'A7': 'g'}
        self.answer = 'abcdefg'
        self.max_score = 28


    def read(self):
        """
        To Read CSV file
        :return:
        """

        list1=[]

        reader = csv.reader(self.file_read)

        for row in reader:
            self.students.append(row)
            print(row)

        # Prepare two list for email and card_label
        for i in range(len(self.students)):
            student = self.students[i]
            stu_length = len(student) -1
            #print("student len :",+stu_length)
            chk_eml = student[stu_length]


            if chk_eml in self.emails :

                pass

            else:
                list2 = []
                for j in range(len(student)):
                   #print("j:",j)
                  if j < stu_length:
                    #self.card_labels.append(student[j])
                    #print("card lables :",self.card_labels)
                    list2.append(student[j])
                    #print("list 2:",list2)
                  else:
                    self.emails.append(student[j])

                    #print("card email :", self.emails)
                       #list1.append(list2)
                print("full list 2 :",list2)
                list1.append(list2)
            print("list 1:",list1)
        # Distribute list in the chunk of 5
        #self.card_labels = self.split_list(self.card_labels, 5)
        self.card_labels = list1
        print("card label list :",self.card_labels)

        print("split list :",self.card_labels)
        print("email ids :",self.emails)
    def compute_score(self):
        """
        To compute score for each card_label
        The output format of the csv file will be:
        <student id>, <score>
        :return:
        """
        scores = []
        for card_label in self.card_labels:
            answer_string = self.transform_card_order_to_string(card_label)
            incorrect_cards = self.levenshtein_score(answer_string)
            correct_cards = len(self.code_map) - incorrect_cards
            print("correct card Arranged:",+correct_cards)
            print("incorrect card Arranged:",incorrect_cards)
            score = (correct_cards * 4) - (incorrect_cards * 2)
            scores.append(score)

        self.scores = scores

    def sum(self):
        print("Avg")
        average = float(sum(self.scores) / 9)
        deviation = []
        for z in self.scores:
            deviation.append(z - average)

        square = []
        for z in deviation:
            square.append(z * z)

        mean = sum(square) / len(square)

        standard_dev = sqrt(sum(square) / (len(square) - 1))
        print("the average  deviation is :", square)
        print("the standard deviation ", sum)
        print(average)


    def write_student_scores(self):
        """
        To write score in CSV file
        :return:
        """
        print("Data in file write : ",self.emails, self.card_labels)
        with open('writefile.csv', 'w', newline='') as csvfile:

            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            i = 0
            for score in self.scores:
                percent = (score / self.max_score) * 100
                spamwriter.writerow([self.emails[i]] + [str(score)] + [str(percent)])
                i += 1

    def split_list(self, alist, wanted_parts=1):
        ''' To split list in specified chunks '''
        length = len(alist)
        return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]

file_read = open("student_responses.csv", "r")
child = ChildClass(file_read)

child.read()
child.compute_score()
child.write_student_scores()

child.sum()

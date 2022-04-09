import re


class project:
    def __init__(self, Title, details, total_target, start_date, end_date, email):
        self.Title = Title
        self.details = details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date
        self.email = email

    def create_project(self):

        create = open("project_data.txt", 'a')
        create.write(self.Title+':'+self.details+':'+self.total_target+':' +
                     self.start_date+':'+self.end_date+':'+self.email + '\n')
        create.close()

    @staticmethod
    def view_projects():
        print("This is your projects")

        try:
          projects = open("project_data.txt", 'r')

          for project in projects:
             split_proj = project.split(":")
             for item in split_proj:
                 print(item)
             print("=====================")

        except FileNotFoundError:
          print("file not found", FileNotFoundError)

    @staticmethod
    def search_project():
        date_regex = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        print("please write start and end date to search")
        search_start_date = input("please enter start date:")
        search_end_date = input("please enter end date:")
        while not re.search(date_regex, search_start_date) and re.search(date_regex, search_end_date):
            search_start_date = input("please enter valid start date:")
            search_end_date = input("please enter valid end date:")

        file = open("project_data.txt", 'r')
        for data in file:
            data_splitted = data.split(":")
            if data_splitted[3] == search_start_date and data_splitted[4] == search_end_date:
                print("========================")
            return data

        return None
    @staticmethod
    def update_project(email):
        new_list = []
        date_regex = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        old_Title = input("please Enter project title: ")
        while not old_Title.isalnum():
            old_Title = input("please Enter project title: ")

        try:
          data_updated = open('project_data.txt', 'r')
          for data in data_updated:
             data_splitted = data.split(':')
             mail = data_splitted[5]
             email1 = email+'\n'
             if email1 == data_splitted[5] and old_Title == data_splitted[0]:
                print("Change yout old Title : ", data_splitted[0], "To")
                new_Title = input()
                while not new_Title.isalnum():
                    print("please enter a valid title:")
                    new_Title = input()

                print("Change yout old Details : ", data_splitted[1], "To")
                new_Details = input()
                while not new_Details.isalnum():
                    print("please enter a valid Details:")
                    new_Details = input()
                print("Change your Total target : ", data_splitted[2], "To")
                new_total_target = input()
                while not new_total_target.isnumeric():
                    print("please enter a numeric target:")
                    new_total_target = input()
                print("Change yout old Start_date : ", data_splitted[3], "To")
                new_start_date = input()
                while not re.search(date_regex, new_start_date):
                    print("enter a valid date:")
                    new_start_date = input()

                print("Change yout old end_date : ", data_splitted[4], "To")
                new_end_date = input()
                while not re.search(date_regex, new_end_date):
                    print("please enter a valid date")
                    new_end_date = input()

                data_splitted[0] = new_Title
                data_splitted[1] = new_Details
                data_splitted[2] = new_total_target
                data_splitted[3] = new_start_date
                data_splitted[4] = new_end_date

             joined_data = ':'.join(data_splitted)
             new_list.append(joined_data)

        
          my_data = ''.join(new_list)

          update_file = open('project_data.txt', 'w')
          update_file.write(my_data)
          update_file.close()

        except FileNotFoundError:
            print("file not found ", FileNotFoundError)


    @staticmethod
    def delete_project(email):  
       
      old_Title=input("please Enter project title: ")
      new_list =[]

      try:
        data_updated=open('project_data.txt','r')
        for data in data_updated:
           data_splitted=data.split(':')
           mail=data_splitted[5] 
           email1=email+'\n'
           if data_splitted[5]==email1  and old_Title==data_splitted[0]:
              data_splitted.clear()
           
           joined_data=':'.join(data_splitted)
           new_list.append(joined_data)


        
     
        my_data=''.join(new_list)

        
        update_file=open('project_data.txt','w')
        update_file.write(my_data)
        update_file.close()
        print("===========================")
        print("You delete it successfully")
        print("============================")
    

               
              
      except FileNotFoundError:
          print("file not found ",FileNotFoundError)
                     

  


def take_inputs(email):
        date_regex = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        Title = input("please enter a project Title: ")
        file = open("project_data.txt", 'r')
        for data in file:
            data_validation = data.split(":")
        while data_validation[0] == Title:
            print("this Title is already exists:")
            print("=================================")
            Title = input("please enter a valid Title:")
            print("=================================")
        while not Title.isalnum():
            Title = input("please enter a valid Title: ")
        details = input("please enter some details about project : \n")
        while not details.isalpha():
            details=input("please enter valid details about project:\n")
        total_target = input("please enter total target:")
        while total_target.isalpha():
            total_target = input("please enter numeric total target: \n")
        start_date = input("please enter start date for the project: \n")
        while not re.search(date_regex, start_date):
            start_date = input("please enter start date:")
        end_date = input("please enter end date:")
        while not re.search(date_regex, end_date):
            end_date = input("please enter an end date:")

        new_project=project(Title,details,total_target, start_date,end_date,email)
        new_project.create_project()


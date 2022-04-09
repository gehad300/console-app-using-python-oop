import project
import re

def sub_menue(email):
    my_crud = {
         "create_project": 1,
           "update_project": 2,
           "view_projects":3,
           "delete":4,
           "search":5,
           "exit":6
             }
    print("please choose from 1 to 6: ")
    for key,value in my_crud.items():
      print(f"{key}:{value}")
    user_choice=int(input("your choice will be : \n"))
      
    if user_choice ==my_crud["create_project"]:
           project.take_inputs(email)
    elif user_choice==my_crud["update_project"]:
         
      project.project.update_project(email)
    elif user_choice==my_crud["view_projects"]:
          project.project.view_projects()

    elif user_choice ==my_crud["delete"]:
       project.project.delete_project(email)
        

    elif user_choice==my_crud["search"]:
          
          project_data=project.project.search_project()
          if project_data==None:
              print("not found")
          else:
              print(project_data)
    elif user_choice==my_crud["exit"]:
          exit()
   
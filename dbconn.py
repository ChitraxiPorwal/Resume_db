import psycopg2

hostname = '127.0.0.1'
database = 'Resume'
username = 'postgres'
pwd = 'porwal'
port_id = 5432
conn = None

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
        return conn 
    
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        print(error)

def insert_personal_details():
    try:
        user_id = int(input("Enter user id:"))
        user_name = input("Enter user name:")
        email = input("Enter user email:")
        phone = input("Enter user phone:")
        github = input("Enter user github:")
        linkedin = input("Enter user linkedin:")
        
        connection = get_db_connection()
        if connection:
            try:
                cur = connection.cursor()
                
                insert_personal_details = '''
                    INSERT INTO personal_details(user_id, user_name, email, phone, github, linkedin) 
                    VALUES(%s, %s, %s, %s, %s, %s)
                '''
                cur.execute(insert_personal_details, (user_id, user_name, email, phone, github, linkedin))
                connection.commit()
            except Exception as error:
                print(f"Error executing the insert query: {error}")
            finally:
                connection.close()
                
        else:
            print("Failed to connect to the database.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for user id.")
  
  
def insert_objective_details():
    try:
        obj_id = int(input("Enter objective id:"))
        objective = input("Enter objective name:")
        user_id = input("Enter user_id to connect via foreign key:")
        
        connection = get_db_connection()
        if connection:
            try:
                cur = connection.cursor()
                
                insert_objective_details = '''
                    INSERT INTO objective_details(obj_id, objective, user_id) 
                    VALUES(%s, %s, %s)
                '''
                cur.execute(insert_objective_details, (obj_id, objective, user_id))
                connection.commit()
            except Exception as error:
                print(f"Error executing the insert query: {error}")
            finally:
                connection.close()
                
        else:
            print("Failed to connect to the database.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for user id.")
        
def insert_educational_details():
    try:
        edu_id = int(input("Enter education id:"))
        institution = input("Enter institution name:")
        programm = input("Enter program studied:")
        mark = input("Enter mark obtained:")
        user_id = input("Enter user_id to connect via foreign key:")
        
        connection = get_db_connection()
        if connection:
            try:
                cur = connection.cursor()
                
                insert_educational_details = '''
                    INSERT INTO educational_details(edu_id, institution, programm, mark, user_id) 
                    VALUES(%s, %s, %s, %s, %s)
                '''
                cur.execute(insert_educational_details, (edu_id, institution, programm, mark, user_id))
                connection.commit()
            except Exception as error:
                print(f"Error executing the insert query: {error}")
            finally:
                connection.close()
                
        else:
            print("Failed to connect to the database.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for user id.")

def insert_work_experiences():
    try:
        work_id = int(input("Enter work id:"))
        company = input("Enter company name:")
        post = input("Enter post:")
        user_id = input("Enter user_id to connect via foreign key:")
        
        connection = get_db_connection()
        if connection:
            try:
                cur = connection.cursor()
                
                insert_work_experiences = '''
                    INSERT INTO work_experiences(work_id, company, post, user_id) 
                    VALUES(%s, %s, %s, %s)
                '''
                cur.execute(insert_work_experiences, (work_id, company, post, user_id))
                connection.commit()
            except Exception as error:
                print(f"Error executing the insert query: {error}")
            finally:
                connection.close()
                
        else:
            print("Failed to connect to the database.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for user id.")

def insert_project_details():
    try:
        pro_id = int(input("Enter project id:"))
        proj = input("Enter project name:")
        tech = input("Enter technology used:")
        user_id = input("Enter user_id to connect via foreign key:")
        
        connection = get_db_connection()
        if connection:
            try:
                cur = connection.cursor()
                
                insert_project_details = '''
                    INSERT INTO project_details(pro_id, proj, tech, user_id) 
                    VALUES(%s, %s, %s, %s)
                '''
                cur.execute(insert_project_details, (pro_id, proj, tech, user_id))
                connection.commit()
            except Exception as error:
                print(f"Error executing the insert query: {error}")
            finally:
                connection.close()
                
        else:
            print("Failed to connect to the database.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for user id.")
       
       
def insert_skills_details():
    try:
        ski_id = int(input("Enter skill id:"))
        skill = input("Enter skills :")
        user_id = input("Enter user_id to connect via foreign key:")
        
        connection = get_db_connection()
        if connection:
            try:
                cur = connection.cursor()
                
                insert_skills_details = '''
                    INSERT INTO skills_details(ski_id, skill, user_id) 
                    VALUES(%s, %s, %s, %s)
                '''
                cur.execute(insert_skills_details, (ski_id, skill, user_id))
                connection.commit()
            except Exception as error:
                print(f"Error executing the insert query: {error}")
            finally:
                connection.close()
                
        else:
            print("Failed to connect to the database.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for user id.")
           
def insert_award_achievements():
    try:
        awa_id = int(input("Enter award id:"))
        award = input("Enter awards :")
        user_id = input("Enter user_id to connect via foreign key:")
        
        connection = get_db_connection()
        if connection:
            try:
                cur = connection.cursor()
                
                insert_award_achievements = '''
                    INSERT INTO award_achievements(awa_id, award, user_id) 
                    VALUES(%s, %s, %s)
                '''
                cur.execute(insert_award_achievements, (awa_id, award, user_id))
                connection.commit()
            except Exception as error:
                print(f"Error executing the insert query: {error}")
            finally:
                connection.close()
                
        else:
            print("Failed to connect to the database.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for user id.")

def insert_hobbies_interests():
    try:
        hob_id = int(input("Enter hobby id:"))
        hobby = input("Enter hobbies :")
        user_id = input("Enter user_id to connect via foreign key:")
        
        connection = get_db_connection()
        if connection:
            try:
                cur = connection.cursor()
                
                insert_hobbies_interests = '''
                    INSERT INTO hobbies_interests(hob_id, hobby, user_id) 
                    VALUES(%s, %s, %s)
                '''
                cur.execute(insert_hobbies_interests, (hob_id, hobby, user_id))
                connection.commit()
            except Exception as error:
                print(f"Error executing the insert query: {error}")
            finally:
                connection.close()
                
        else:
            print("Failed to connect to the database.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for user id.")








'''
insert_personal_details()  
insert_objective_details
insert_educational_details()
insert_work_experiences
insert_project_details
insert_skills_details
insert_award_achievements
insert_hobbies_interests
'''










'''
        insert_personal_details = 
            INSERT INTO personal_details(user_id, user_name, email, phone, github, linkedin) 
            VALUES(%s, %s, %s, %s, %s, %s)
            
        insert_user_values = [
            (1, 'James', 'james@gmail.com', '1234567890', 'james/1234', '1234/james'),
            (2, 'John', 'john@gmail.com', '1234567890', 'john/1234', '1234/john'),
            (3, 'Jony', 'jony@gmail.com', '1234567890', 'jony/1234', '1234/jony'),
            (4, 'Jase', 'jase@gmail.com', '1234567890', 'jase/1234', '1234/jase')
        ]
    '''
        #for record in insert_user_values:
        #cur.execute(insert_personal_details, record)
    
            #update_script = 'UPDATE person SET salary = salary + (salary*0.5)'
            #cur.execute(update_script)

            #delete_script 'DELETE FROM employee WHERE name = %s'
            #delete_record = ('James',)
            #cur.execute(delete_script, delete_record)
'''
    user_id = int(input(Enter user id:))
    user_name = input(Enter user name:)
    email = input(Enter user email:)
    phone = input(Enter user phone:)
    github = input(Enter user github:)
    linkedin = input(Enter user linkedin:)
'''
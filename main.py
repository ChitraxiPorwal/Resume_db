import psycopg2.extras
import dbconn
from fpdf import FPDF

connection = dbconn.get_db_connection()

class Resume:
    def display_resume(self):
        if connection:
            try:
                with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    while True:
                        id_choice = input("Which id resume do you want (or enter 'no' stop):")
            
                        if id_choice.lower() == 'no':  
                            break           
                        try:
                            id_choice = int(id_choice)
                        except ValueError:
                            print("Please enter a valid integer for the user ID.")
                            continue
            
                        cur.execute('''Select * from personal_details pd 
                                    FULL OUTER JOIN objective_details od ON pd.user_id = od.user_id 
                                    FULL OUTER JOIN educational_details ed ON pd.user_id = ed.user_id 
                                    FULL OUTER JOIN work_experiences we ON pd.user_id = we.user_id 
                                    FULL OUTER JOIN project_details pdd ON pd.user_id = pdd.user_id 
                                    FULL OUTER JOIN skills_details sd ON pd.user_id = sd.user_id 
                                    FULL OUTER JOIN award_achievements aa ON pd.user_id = aa.user_id 
                                    FULL OUTER JOIN hobbies_interests hi ON pd.user_id = hi.user_id 
                                    WHERE pd.user_id = %s''' , (id_choice,))
                    
                        record = cur.fetchone()

                        if record:
                            dis = ("********************RESUME********************")
                            dis += (f"Name: {record['user_name']}")
                            dis += (f"Email: {record['email']}")
                            dis += (f"Phone: {record['phone']}")
                            dis += (f"GitHub: {record['github']}")
                            dis += (f"LinkedIn: {record['linkedin']}\n\n")
                    
                            dis += ("Objective:")          
                            dis += (f"Objective {record['objective']}\n\n")
                        
                            dis += ("Educational Details:")          
                            dis += (f"Institution: {record['institution']}")
                            dis += (f"Program: {record['programm']}")
                            dis += (f"Mark: {record['mark']}\n\n")
    
                            dis += ("Work Experiences:")          
                            dis += (f"Company: {record['company']}")
                            dis += (f"Post: {record['post']}\n\n")

                            dis += ("Project:")          
                            dis += (f"proj: {record['proj']}")
                            dis += (f"tech: {record['tech']}\n\n")

                            dis += ("Skills:")          
                            dis += (f"skill: {record['skill']}\n\n")

                            dis += ("Award and Achievements:")          
                            dis += (f"award: {record['award']}\n\n")

                            dis += ("Hobbies and Interests:")          
                            dis += (f"hobby: {record['hobby']}\n\n")

                        else:
                            print(f"No resume found with user_id = {id_choice}")

                        print(dis)
                        return dis
                    
            except Exception as error:
                print(f"Error executing query: {error}")
            finally:
                connection.close()
        else:
            print("Failed to connect to the database.")
        
        
    def pdf(self, content, filename="123456.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=13) 
        for line in content.split("\n"):
            pdf.cell(200, 10, txt=line, ln=True)
        pdf.output(filename)
        print("According to information you have entered resume have been generated as the name:" + filename + ".pdf")
   
    
    
    






    
#display_resume()

         
if __name__ == "__main__":
    res = Resume()
    res_con = res.display_resume()      
    res.pdf(res_con)   
  
    
    
    
    
    
#print(record['user_name'],"\n" ,record['email'],"\n" ,record['phone'],"\n" ,record['email'],"\n" ,record['github'],"\n" ,record['linkedin'])

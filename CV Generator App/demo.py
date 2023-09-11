from ctypes import alignment
from tkinter import *
from turtle import title
from cv2 import add
import pyqrcode
from fpdf import FPDF 
from tkinter import messagebox

class PDFCV(FPDF):
    def header(self):
        self.image("mywebsite.png", 10, 8, 33, title="Portfolio Site")

    def footer(self):
        pass

    def generate_cv(self, name, email, phone_number, address, skills, work_experience, education, about_me):
        self.add_page()
        self.ln(20)

        # Displaying the name
        self.set_font("Arial", "B", 26)
        self.cell(0, 10, name, new_x="LMARGIN", new_y="NEXT", align = "C")

        # Adding contact information header
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Contact Inforamtion", new_x="LMARGIN", new_y="NEXT", align = "L")

        # Adding the contact information
        self.set_font("Arial", "", 10)
        self.cell(0, 5, "Email: {}".format(email), new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, "Phone: {}".format(phone_number), new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, "Address: {}".format(address), new_x="LMARGIN", new_y="NEXT")

        # Skills
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Skills", new_x="LMARGIN", new_y="NEXT", align = "L")
        
        # Adding the skills
        self.set_font("Arial", "", 10)
        for skill in skills:
            self.cell(0, 5, f"- {skill}", new_x="LMARGIN", new_y="NEXT", align = "L")

        # Work Experience
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Work Experience", new_x="LMARGIN", new_y="NEXT", align = "L")
        
        # Adding the skills
        self.set_font("Arial", "", 10)
        for experience in work_experience:
            self.cell(0, 5, "{}: {}".format(experience["title"], experience["description"]), new_x="LMARGIN", new_y="NEXT", align = "L")

        # Education
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Education", new_x="LMARGIN", new_y="NEXT", align = "L")
        
        # Adding the education
        self.set_font("Arial", "", 10)
        for education_item in education:
            self.cell(0, 5, "{}: {}".format(education_item["degree"], education_item["university"]), new_x="LMARGIN", new_y="NEXT", align = "L")

        # About Me Header
        self.ln(10)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "About Me", new_x="LMARGIN", new_y="NEXT", align = "L")
        
        # About Me
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 5, about_me)

        self.output("cv.pdf")



def generate_cv_pdf():
    name = entry_name.get()
    email = entry_email.get()
    phone_number = entry_phone.get()
    address = entry_address.get()
    website = "https://" + entry_website.get()
    skills = entry_skills.get("1.0", END).strip().split("\n")
    work_experience = []
    education = []
    
    work_experience_lines = entry_experience.get("1.0", END).strip().split("\n")
    for line in work_experience_lines:
        title, description = line.split(":")
        work_experience.append({"title":title.strip(), "description": description.strip()})

    education_lines = entry_education.get("1.0", END).strip().split("\n")
    for line in education_lines:
        degree, university = line.split(":")
        education.append({"degree": degree.strip(), "university": university.strip()})

    about_me = entry_about_me.get("1.0", END)

    # Create QR Code 
    qrcode = pyqrcode.create(website)
    qrcode.png("mywebsite.png", scale=6)

    if not name or not email or not phone_number or not address or not skills or not education or not work_experience or not about_me:
        messagebox.showerror("Error", "Please fill in all the details")
        return 
    
    cv = PDFCV()
    cv.generate_cv(name, email, phone_number, address, skills, work_experience,
                    education, about_me)




window = Tk()
window.title("CV Generator")

label_name = Label(window, text = "Name: ")
label_name.pack()
entry_name = Entry(window)
entry_name.pack()

label_email = Label(window, text = "Email: ")
label_email.pack()
entry_email = Entry(window)
entry_email.pack()

label_phone = Label(window, text = "Phone: ")
label_phone.pack()
entry_phone = Entry(window)
entry_phone.pack()

label_address = Label(window, text = "Address: ")
label_address.pack()
entry_address = Entry(window)
entry_address.pack()

label_website = Label(window, text = "Website: ")
label_website.pack()
entry_website = Entry(window)
entry_website.pack()

label_skills = Label(window, text = "Skills(Enter one skill per line)")
label_skills.pack()
entry_skills = Text(window, height= 5)
entry_skills.pack()

label_education = Label(window, text = "Education(One per line in format 'Degree': 'University')")
label_education.pack()
entry_education = Text(window, height= 5)
entry_education.pack()

label_experience = Label(window, text = "Experience(Enter one per line in format 'Job Title': 'Description')")
label_experience.pack()
entry_experience = Text(window, height= 5)
entry_experience.pack()

label_about_me = Label(window, text = "About Me")
label_about_me.pack()
entry_about_me = Text(window, height= 5)
entry_about_me.pack()

button_generate = Button(window, text = "Generate CV", command= generate_cv_pdf)
button_generate.pack()

window.mainloop()
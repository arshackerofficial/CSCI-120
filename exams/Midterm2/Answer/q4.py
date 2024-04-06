# 815805
def create_and_save_student(name, age, gender, marks):
    # WRITE YOUR CODE HERE
    """
    Function to create a Student object and save details.

    Parameters:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - gender (str): The gender of the student.
    - marks (dict): A dictionary containing subject names as keys and corresponding marks as values.

    Returns:
    - Student: The Student object with the provided details.
    """

    # Student class definition
    class Student:
        """
        Create a claass named Student with the folloing methods as provided below
        """
        name = ""
        age = 0
        marks = {}
        gender = ""

        # __init__ method definition
        """
        Initializes a new student record with the provided attributes.

        Parameters:
        - name (str): The name of the student.
        - age (int): The age of the student.
        - gender (str): The gender of the student.
        - marks (dict): A dictionary containing subject names as keys and corresponding marks as values.
        """

        def __init__(self, name, age, gender, marks):
            self.name = name
            self.age = age
            self.marks = marks
            self.gender = gender

        # calculate_total_marks method definition
        """
        Calculates the total marks obtained by the student across all subjects.

        Returns:
        - int: The total marks obtained.
        """

        def calculate_total_marks(self):
            total = 0
            for i in self.marks:
                total += self.marks[i]
            return total

        # calculate_total_percentage method definition
        """
        Calculates the percentage of marks obtained by the student.

        Returns:
        - float: The percentage of marks.
        """

        def calculate_total_percentage(self):
            total = 0
            self.calculate_total_marks()/len(self.marks)+1

            return total

        # display_student_details method definition
        """
        Displays all the details of the student including name, age, gender, marks obtained in each subject, 
        total marks, and percentage. If total marks > 250, print "Great work!", otherwise print "Keep trying!".

        """

        def display_student_details(self):
            print(self.marks)
            if self.calculate_total_marks() > 250:
                print("Great work")
            else:
                print("Keep Trying")

    # DONT WRITE ANYTHING BELOW THIS
    return Student(name, age, gender, marks)


def main():
    # Dummy data for two students
    student1_details = {
        "name": "John Doe",
        "age": 17,
        "gender": "Male",
        "marks": {"Math": 90, "Science": 85, "History": 75}
    }
    student2_details = {
        "name": "Jane Smith",
        "age": 18,
        "gender": "Female",
        "marks": {"Math": 75, "Science": 60, "History": 75}
    }

    # Create and save details for student 1
    student1 = create_and_save_student(**student1_details)

    # Display details for student 1
    student1.display_student_details()
    print()

    # Create and save details for student 2
    student2 = create_and_save_student(**student2_details)


if __name__ == "__main__":
    main()

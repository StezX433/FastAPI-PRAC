from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

students = {
    "S001": {"name": "John Doe", "marks": 85, "grade": "A"},
    "S002": {"name": "Jane Smith", "marks": 90, "grade": "S"},
    "S003": {"name": "Alice Johnson", "marks": 78, "grade": "B"}
    
}

#input schema
class submission(BaseModel):
    name: str
    marks: int
    subject: str
    grade: str



@app.get("/students/{student_id}")
def get_student(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    
    
    
    return students[student_id]

@app.post("/submit-marks")
def submit_marks(submission: submission):
    
    if submission.marks < 0 or submission.marks > 100:
        raise HTTPException(status_code=400, detail="Marks must be between 0 and 100")
    if submission.grade not in ["S", "A", "B", "C", "D", "E", "F"]:
        raise HTTPException(status_code=400, detail="Invalid grade. Must be one of S, A, B, C, D, E, F")
    if submission.subject not in ["Math", "Science", "English", "History"]:
        raise HTTPException(status_code=400, detail="Invalid subject. Must be one of Math, Science, English, History")
    if submission.name.strip() == "":
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    
    
    student_id = f"S{len(students) + 1:03d}"  # Generate a new student ID
    students[student_id] = {
        "name": submission.name,
        "marks": submission.marks,
        "grade": submission.grade
    }
    return {"message": "Marks submitted successfully", "student_id": student_id}

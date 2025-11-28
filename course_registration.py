# course_registration.py - Course Registration Module

class CourseRegistration:
    def __init__(self):
        self.registered_courses = []
        self.max_courses_per_student = 5
    
    def register_course(self, student_id, course_id, course_name):
        """Register a student for a course"""
        if len(self.registered_courses) >= self.max_courses_per_student:
            return {"success": False, "message": "Maximum course limit reached"}
        
        self.registered_courses.append({
            "student_id": student_id,
            "course_id": course_id,
            "course_name": course_name,
            "status": "active"
        })
        
        return {"success": True, "message": f"Student {student_id} registered for {course_name}"}
    
    def unregister_course(self, student_id, course_id):
        """Unregister a student from a course"""
        self.registered_courses = [
            course for course in self.registered_courses
            if not (course["student_id"] == student_id and course["course_id"] == course_id)
        ]
        return {"success": True, "message": "Course unregistered successfully"}
    
    def get_registered_courses(self, student_id):
        """Get all courses registered by a student"""
        return [c for c in self.registered_courses if c["student_id"] == student_id]
    
    def get_system_status(self):
        """Get the system status - WILL CAUSE MERGE CONFLICT"""
        return "Course Registration System - v1.0 - Active"

if __name__ == "__main__":
    system = CourseRegistration()
    print(system.get_system_status())

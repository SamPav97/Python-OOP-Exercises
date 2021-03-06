class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = int(skills)

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += int(skills_earned)
            return f"{self.name} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if new_language != self.language and int(skills_needed) <= self.skills:
            old = self.language
            self.language = new_language
            return f"{self.name} switched from {old} to {new_language}"
        elif new_language == self.language and int(skills_needed) <= self.skills:
            return f"{self.name} already knows {new_language}"
        else:
            return f"{self.name} needs {skills_needed - self.skills} more skills"

"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without -
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes
you want.
"""
from datetime import datetime, timedelta


class DeadlineError(Exception):
    def __init__(self, message="You are late"):
        self.message = message
        super().__init__(self.message)


class Homework:

    def __init__(self, text_exercise: str, deadline: int):
        self.time_to_creation = datetime.now()
        self.text_exercise = text_exercise
        self.deadline = deadline

    def deadline_pass(self):
        return self.time_to_creation + timedelta(days=self.deadline) >= datetime.now()


class Student:

    def __init__(self, second_name, first_name):
        self.second_name = second_name
        self.first_name = first_name

    def do_homework(self, hw: Homework, solution: str):
        complete_hw = CompleteHomework(self, hw, solution, hw.text_exercise, hw.deadline)
        if not complete_hw.deadline_pass():
            raise DeadlineError
        return complete_hw


class CompleteHomework(Homework):
    def __init__(self, student: Student, hw: Homework, solution: str, text_exercise: str, deadline: int):
        super().__init__(text_exercise, deadline)
        self.author = student
        self.hw = hw
        self.solution = solution


class Teacher:
    homework_done = dict()

    def __init__(self, second_name, first_name):
        self.second_name = second_name
        self.first_name = first_name

    @classmethod
    def create_homework(cls, text_ex: str, deadline: int):
        hw = Homework(text_ex, deadline)
        cls.homework_done[hw] = []
        return hw

    @classmethod
    def reset_results(cls):
        cls.homework_done = dict()

    @classmethod
    def check_homework(cls, comp_hw: CompleteHomework):
        if comp_hw not in cls.homework_done[comp_hw.hw] and len(comp_hw.solution) > 5:
            cls.homework_done[comp_hw.hw].append(comp_hw)
        cls.homework_done[comp_hw] = comp_hw.solution
        return len(comp_hw.solution) > 5

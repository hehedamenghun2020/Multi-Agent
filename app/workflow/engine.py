from app.agents.planner import Planner
from app.agents.executor import Executor
from app.agents.researcher import Researcher
from app.agents.qa import QA
from app.memory.memory import Memory

class WorkflowEngine:
    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.researcher = Researcher()
        self.qa = QA()
        self.memory = Memory()

    def run(self, task):
        self.memory.add("user_task", task)

        steps = self.planner.run(task)

        results = []
        for step in steps:
            context = self.memory.get_all()
            info = self.researcher.run(step, context)
            result = self.executor.run(step, info)
            self.memory.add("step_result", result)
            results.append(result)

        final = self.qa.run(results)
        return final

from app.workflow.engine import WorkflowEngine

if __name__ == "__main__":
    engine = WorkflowEngine()
    while True:
        task = input("输入复杂任务: ")
        result = engine.run(task)
        print("\n=== FINAL RESULT ===")
        print(result)

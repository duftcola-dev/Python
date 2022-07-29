from alive_progress import alive_bar 
import time


# base test case of alive bar

task_eta = 100
# with alive_bar(total=100,dual_line=True,title="installation:") as bar:
#     for _ in range(task_eta):
#         time.sleep(0.05)
#         bar()

# test case with several tasks
tasks = 4
task_eta = [100,200,50,100]
task_title = ["fetching packages","downloading","extracting packages","installation"]

for task in range(tasks):
    with alive_bar(total=task_eta[task],dual_line=True,title=task_title[task]) as bar:
        for _ in range(task_eta[task]):
            time.sleep(0.05)
            bar()

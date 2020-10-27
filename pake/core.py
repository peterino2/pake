import colorama
colorama.init(autoreset=True)

# --- singletons ---
g_PakeJobs = {}

def show_jobs():
    global g_PakeJobs
    
    word = "are"
    s = "s"
    if len(g_PakeJobs) == 1:
        word = "is"
        s = ""
    print(f"There {word} {len(g_PakeJobs)} job{s} registered:")
    for name, job in g_PakeJobs.items():
        if job.docs is not None:
            print(f"    {name} - {job.docs}")
        else:
            print(f"    {name}")


def run_jobs():
    for name, job in g_PakeJobs.items():
        job.func()



class jobclass:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        self.docs = func.__doc__


def job(func):
    def wrapper_job(*args, **kwargs):
        func(*args, **kwargs)
    global g_PakeJobs
    g_PakeJobs[func.__name__] = jobclass(func)

    return wrapper_job


@job
def test_job():
    print("[Job running]")

@job
def test_job2():
    "a docstring"
    print("[Job2 running]")

@job
def test_job3():
    print("[Job2 running]")

if __name__ == "__main__":
    show_jobs()
    run_jobs()

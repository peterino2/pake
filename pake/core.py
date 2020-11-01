import colorama
import argparse
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
        if job.desc is not None:
            print(f"    {name} - {job.desc}")
        else:
            print(f"    {name}")


def run_jobs():
    for name, job in g_PakeJobs.items():
        print(f"Running Pake job {name}")
        job.func()

class jobclass:
    def __init__(
            self, 
            func, 
            desc=None,
            depends=None,
            fdepends=None
        ):
        self.func = func
        self.name = func.__name__
        self.docs = func.__doc__

        self.desc = desc

        self.depends = depends if depends is not None else []
        self.fdepends = fdepends if fdepends is not None else []

    def check_deps(self):
        pass

def job(*args, **kwargs):
    def decorator(f):
        global g_PakeJobs
        g_PakeJobs[f.__name__] = jobclass(f, **kwargs)
        return f
    return decorator


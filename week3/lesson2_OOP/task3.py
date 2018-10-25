class IT_Company:
    def __init__(self):
        self.dev_list = []

    def __add__(self, worker):
        if worker.years_experience >= 3:
            self.dev_list.append(worker)
        else:
            print('\tSorry, not enough experience')

    def __str__(self):
        return '\n\t'.join([str(__) for __ in sorted(self.dev_list, key=lambda worker: worker.years_experience)])

    def dismiss_worker(self, worker_name):
        for worker in self.dev_list:
            if worker.name == worker_name:
                self.dev_list.remove(worker)
                return print("\tWorker {name} deleted".format(name=worker_name))
        return print("\tCan`t find such worker")


if __name__ == '__main__':

    from task1 import *

    com_base = IT_Company()
    worker1 = PythonDeveloper('Boris', 12)
    worker2 = RubyDeveloper('Misha', 1 )
    worker3 = JavaDeveloper('Roma', 3 )
    worker4 = PythonDeveloper('Sershz', 4)
    worker5 = RubyDeveloper('Pioter', 2)
    worker6 = JavaDeveloper('Brody', 7)

    print('Add worker to IT_Company:')
    com_base + worker1
    com_base + worker2
    com_base + worker3
    com_base + worker4
    com_base + worker5
    com_base + worker6

    print('List of worker:\n\t', com_base)
    print()

    print('Delete exist worker:')
    com_base.dismiss_worker('Boris')
    print('Delete non-existent worker:')
    com_base.dismiss_worker('Sasha')

    print('List of worker:\n\t', com_base)

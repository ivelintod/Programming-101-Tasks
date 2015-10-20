import json
import os


class DResolver:

    def __init__(self, packages, dependencies):
        packages = DResolver.jsonize_input(packages)
        dependencies = DResolver.jsonize_input(dependencies)
        with open('{}'.format(packages)) as f:
            self.packages = json.load(f)
        with open('{}'.format(dependencies)) as f:
            self.dependencies = json.load(f)

        self.report = []
        self.visited = set()

    @staticmethod
    def jsonize_input(inp):
        if not inp.endswith('.json'):
            inp = inp + '.json'
        return inp

    def get_installed_modules(self):
        installed_modules = set()
        for file in os.listdir(os.path.join('installed_modules')):
            installed_modules.add(file)
        return installed_modules

    def resolve_dependency(self, dep):
        installed_modules = self.get_installed_modules()
        not_installed = list()
        if dep not in installed_modules:
            self.report.append('Installing {}.'.format(dep))
            next = None
            if self.packages[dep]:
                next = 'In order to install {}, we need '.format(dep)
                for d in self.packages[dep]:
                    next += d + ' and '
                    if d not in installed_modules:
                        not_installed.append(d)

                next = next.strip(' and ')
                next += '. '
                already_resolved = installed_modules.intersection(set(self.packages[dep]))
                if already_resolved:
                    for d in already_resolved:
                        next += d.title() + ' and '
                    next = next.strip(' and ')
                    next += ' already installed'

            with open(os.path.join('installed_modules/') + '{}'.format(dep), 'w') as f:
                f.write('')
            if next:
                self.report.append(next)
            for d in not_installed:
                self.resolve_dependency(d)


    def resolve(self):
        for dep in self.dependencies['dependencies']:
            self.resolve_dependency(dep)
        self.report.append('All done')
        return '\n'.join(self.report)


d = DResolver('all_packages', 'dependencies')
#print(d.packages)
#print(d.get_installed_modules())
print(d.resolve())


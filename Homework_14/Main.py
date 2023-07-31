from Project import Project

PATH = 'users.json'

with Project.get_users_from_json(PATH) as project:
    project.run()

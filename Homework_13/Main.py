from Project import Project

with Project.get_users_from_json() as project:
    project.run()

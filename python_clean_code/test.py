def wrong_user_display(user_metadata: dict={'name': 'john', 'age': 30}):
    name = user_metadata.pop('name')
    age = user_metadata.pop('age')
    return "{} {}".format(name, age)

wrong_user_display()


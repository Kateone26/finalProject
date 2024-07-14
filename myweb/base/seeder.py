from .models import Skill, Category


def seeder_func():
    skills = ['JavaScript', 'WordPress', 'Rest API', 'MySQL', 'TypeScript', 'PHP', 'Python', 'C++', 'Kotlin', 'HTML', 'CSS', 'Java']
    categories = ['FrontEnd', 'BackEnd', 'Cloud', 'AI', 'Mobile']

    for skill in skills:
        if not Skill.objects.filter(name=skill):
            new_skill = Skill(name=skill)
            new_skill.save()

    for category in categories:
        if not Category.objects.filter(name=category):
            new_category = Category(name=category)
            new_category.save()

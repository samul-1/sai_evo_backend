from courses.models import EventTemplateRule, Exercise


def get_exercises_from(template, course=None, pool=None):
    exercises = Exercise.objects.base_exercises()
    if course is not None:
        exercises = exercises.filter(course=course)
    if pool is not None:
        exercises = exercises.filter(pk__in=pool)

    picked_exercises = []
    for rule in template.rules.all():
        rule_qs = exercises.satisfying(rule)

        picked_exercise = rule_qs.exclude(
            pk__in=[e.pk for e in picked_exercises]
        ).get_random()
        picked_exercises.append(picked_exercise)

    return picked_exercises

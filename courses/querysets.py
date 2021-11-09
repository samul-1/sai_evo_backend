import random

from django.db import models
from django.db.models import aggregates
from django.db.models.aggregates import Max, Min


class ExerciseQuerySet(models.QuerySet):
    def base_exercises(self):
        """
        Returns the exercises that don't have a parent foreign key
        (i.e. that aren't a sub-exercise)
        """
        return self.filter(parent__isnull=True)

    def satisfying(self, rule):
        """
        Returns the exercises that satisfy an EventTemplateRule
        """
        from courses.models import EventTemplateRule

        if rule.rule_type == EventTemplateRule.ID_BASED:
            ret_qs = self.filter(pk__in=[e.pk for e in rule.exercises.all()])
        else:  # tag-based rule
            ret_qs = self
            for clause in rule.clauses.all():
                ret_qs = ret_qs.filter(tags__in=[t for t in clause.tags.all()])
            ret_qs = (
                ret_qs.distinct()
            )  # if more than one tag match, an item may be returned more than once
        return ret_qs

    def get_random(self, exclude=None):
        """
        Returns a random exercise from the queryset
        """
        qs = self
        if exclude is not None:
            qs = qs.exclude(pk__in=[e.pk for e in exclude])

        aggregate_id = qs.aggregate(max_id=Max("id"), min_id=Min("id"))
        max_id, min_id = aggregate_id["max_id"], aggregate_id["min_id"]

        picked_id = random.randint(min_id, max_id)

        return qs.filter(pk__gte=picked_id).first()


class SlotModelQuerySet(models.QuerySet):
    def base_slots(self):
        """
        Returns the slots that don't have a parent foreign key
        (i.e. that aren't a sub-slot)
        """
        return self.filter(parent__isnull=True)

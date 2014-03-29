This project should work out of the box as it uses sqllite.

Executing the test generates the following error:

```
$ ./manage.py test
Creating test database for alias 'default'...
E
======================================================================
ERROR: test_can_create_fave_cars (dpb.tests.Test)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/mtford/Playground/django_positions_bug/dpb/tests.py", line 16, in test_can_create_fave_cars
    models.FaveCar(car=self.bmw, person=self.person).save()
  File "/Library/Python/2.7/site-packages/django/db/models/base.py", line 545, in save
    force_update=force_update, update_fields=update_fields)
  File "/Library/Python/2.7/site-packages/django/db/models/base.py", line 573, in save_base
    updated = self._save_table(raw, cls, force_insert, force_update, using, update_fields)
  File "/Library/Python/2.7/site-packages/django/db/models/base.py", line 632, in _save_table
    for f in non_pks]
  File "/Library/Python/2.7/site-packages/positions/fields.py", line 72, in pre_save
    previous_instance = type(model_instance)._default_manager.get(pk=model_instance.pk)
  File "/Library/Python/2.7/site-packages/django/db/models/manager.py", line 151, in get
    return self.get_queryset().get(*args, **kwargs)
  File "/Library/Python/2.7/site-packages/django/db/models/query.py", line 307, in get
    self.model._meta.object_name)
DoesNotExist: FaveCar matching query does not exist.

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (errors=1)
Destroying test database for alias 'default'...
```

from behave import *
from second import Furniture
from second import Box
from second import Packed
from second import Adapter

@given('count of box - "{box_count}" and newsize of box - "{box_newsize}" count of packed - "{packed_count}" and newsize of packed - "{packed_newsize}"')
def step(context, box_count, box_newsize, packed_count, packed_newsize):
    context.box = Box(box_count, box_newsize)
    context.packed = Packed(packed_count, packed_newsize)

@then('Yes')
def step(context):
    assert context.box.fit(context.packed) ==   f"Поместится " \
                                                f"\n"\
                                                f"Высота БЛОКА {context.packed.get_count()}, объём {context.packed.get_newsize()}" \
                                                f"\n"\
                                                f"Высота БОКСА {context.box.get_count()}, объём {context.box.get_newsize()}"


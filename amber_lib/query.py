import collections
import json



class WhereItem(object):
    def __init__(self, operand="", pred=None, items=None):
        self.operand = operand
        self.pred = pred
        self.items = items if items else []

    def to_dict(self):
        return {"operand": self.operand, "pred": self.pred, "items": self.items}

    def to_json(self):
        return json.dumps(self.to_dict())


class Predicate(object):
    def __init__(self, subject, operand=None, value=None):
        self.subject = None
        self.operand = None
        self.value = None

    def to_dict(self):
        return {"subject": self.subject, "operand": self.operand, "value": self.value}

    def to_json(self):
        return json.dumps(self.to_dict())


def And(first, second):
    if not isinstance(second, WhereItem):
        second = WhereItem(items=[second])
    if second.operand and second.operand != "and":
        raise Exception(
            'Second WhereItem has operand: %s, must be empty or "%s"' % (
                second.operand,
                'and'
            )
        )
    second.operand = "and"

    if not isinstance(first, WhereItem):
        first = WhereItem("", first, second)
    else:
        first.items.append(second)

    return first


def Or(first, second):
    if not isinstance(second, WhereItem):
        second = WhereItem(items=[second])
    if second.operand and second.operand != "or":
        raise Exception(
            'Second WhereItem has operand: %s, must be empty or "%s"' % (
                second.operand,
                'or'
            )
        )
    second.operand = "or"

    if not isinstance(first, WhereItem):
        first = WhereItem("", first, second)
    else:
        first.items.append(second)

    return first

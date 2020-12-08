def latest(scores):
    return scores[-1]


def personal_best(scores):
    if scores:
        return max(scores)
    else:
        return scores


def personal_top_three(scores):
    lst = scores
    result = []
    count = 3
    if len(scores) < 3:
        count = len(scores)
    while count >= 1:
      val = max(lst)
      idx = lst.index(val)
      result.append(lst.pop(idx))
      count -= 1
      print(result)
    return result

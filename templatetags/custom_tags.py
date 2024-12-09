from django import template
register = template.Library()

@register.filter
def unit_filter(num):

  # 表示数値の単位変換用：昇順
  UNIT_LIST = [
      { "num": 1E3, "unit": "K" },
      { "num": 1E6, "unit": "M" },
      { "num": 1E9, "unit": "B" },
      { "num": 1E12, "unit": "T"}
  ]

  if num < UNIT_LIST[0]["num"]:
    return num

  # 1000以上は単位変換
  for unit in reversed(UNIT_LIST):
    if num >= unit["num"]:
      return f'{num/unit["num"]:.1f}{unit["unit"]}'
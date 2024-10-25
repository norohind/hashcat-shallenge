#!/usr/bin/env python
expecting_hash = False
def save(a):
  with open("output.txt", 'a', encoding='utf-8') as f:
    f.write(a + '\n')


while True:
  try:
    line = input()
    if expecting_hash:
      save(line)
      expecting_hash = False

    if 'mark_hash' in line:
      expecting_hash = True
      save(line)

    print(line)

  except EOFError:
    break


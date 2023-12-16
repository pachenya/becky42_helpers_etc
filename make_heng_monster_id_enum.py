#
# Hengband monster id enum maker
# by @alicebecky10 (on X)
#
# 2023.12.03(Su) : start.
# 2023.12.16(Sa) : bug fixes and minor fixes.
#

import re

tmpmn = [] # tmp monster names a.k.a. TiMPoMaN.
tmpmnbuilded = []
mondef = []
mondefId = []

def OpenTextList(filename):
  f = open(filename)
  lns = f.readlines()
  f.close()
  return lns

def gaishutsu_check(mname):
  i = 0
  for nm in tmpmn:
    if nm == mname:
      i = i + 1
  return i

def gaishutsu_check_2(mname):
  i = 0
  for nm in tmpmnbuilded:
    if nm == mname:
      i = i + 1
  return i

def usable_char_check(ch):
  is_ok = False
  if "0" <= ch <= "9" or "A" <= ch <= "Z" or \
  "a" <= ch <= "z" or ch == "_":
    is_ok = True
  return is_ok

def build_mon_id(s):
  rval = ""
  ch = ""
  for c in s:
    if usable_char_check(c):
      ch = c
    else:
      ch = "_"
    rval += ch
  rval = re.sub('_+', '_', rval)
  return rval

def read_lib_mondef_line(s, pfx):
  if s[0] == 'N':
    stmp = re.search(r'\d+', s)
    nid = str(stmp.group())
    mondefId.append(nid) # KIWOTSUKETENE!!
  elif s[0] == 'E':
    mn = pfx + s[2:].upper()
    mn = mn.rstrip('\r\n')
    
    gcheckn = gaishutsu_check(mn)
    tmpmn.append(mn) # for gaishutsu_check()

    mn = build_mon_id(mn)

    gcheckn = gcheckn + gaishutsu_check_2(mn)
    tmpmnbuilded.append(mn)
    
    if gcheckn > 0:
      mn = mn + '_' + str(gcheckn+1)
    mondef.append(mn)
    # print(mn)
  return

def WriteToFile(filename):
  with open(filename, mode='w') as f:
    f.write('enum monid_enum {\n')
    i = 0
    for m in mondef:
      txt = '    ' + m + ' = ' + mondefId[i] + ',\n'
      f.write(txt)
      i = i + 1
    f.write('};')
  return

def main():
  monpfx = 'MONID_'
  p = input("Enter prefix. (default 'MONID_')\n")
  if len(p) > 1:
    monpfx = p
  
  mname = OpenTextList('MonsterRaceDefinitions.txt')
  for s in mname:
     read_lib_mondef_line(s, monpfx)
  o = 'mondef-enum.cpp'
  p = input("Enter out filename.(default 'mondef-enum.cpp')\n")
  if len(p) > 1:
    o = p
  WriteToFile(o)
  return

main()

# EOF
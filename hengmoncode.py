import re
import json
import random

# AI生成コード
def remove_jsonc_comments(jsonc_str: str) -> str:
    """
    JSONC文字列からコメントを削除してJSON文字列に変換する。
    - // コメント
    - /* コメント */

    文字列リテラル内のコメント記号は無視されます。
    """
    def replacer(match):
        s = match.group(0)
        # 文字列リテラルはそのまま残す
        if s.startswith('"') or s.startswith("'"):
            return s
        # それ以外（コメント）は削除
        return ''

    # 正規表現パターン（文字列リテラル + コメント）
    pattern = re.compile(
        r'''
        ("(?:\\.|[^"\\])*")       |   # ダブルクオート文字列
        ('(?:\\.|[^'\\])*')       |   # シングルクオート文字列
        (//[^\n\r]*$)             |   # 行コメント
        (/\*[\s\S]*?\*/)              # ブロックコメント
        ''',
        re.VERBOSE | re.MULTILINE
    )
    return re.sub(pattern, replacer, jsonc_str)
#AI 生成コードここまで

monl=[]
monl.append(('x','没キャラ'))
monl.append((' ','\n'))

def ch2monnam(ch):
  cnt=0
  rval = '謎の怪物'
  for m in monl:
    if m[0]==ch:
      cnt+=1
      if random.randrange(cnt)==0:
        rval=m[1]
  return rval

def test():
  s=open('md.jsonc').read() # Hengband monsters file.
  s2=remove_jsonc_comments(s)
  s3=json.loads(s2)
  for na in s3['monsters']:
    cha=na['symbol']['character']
    nam=na['name']['ja']
    monl.append((cha,nam))
  while(True):
    instr=input()
    if len(instr)==0:
      break
    for i in instr:
      print(ch2monnam(i),end=' ')
    print('')

test()

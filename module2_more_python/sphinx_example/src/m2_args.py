import sys
import argparse

# 取得參數最原始的方法 list
print('raw arguments = ' + str(sys.argv), end='\n\n')

# 使用 Python 內建的參數解析
parser = argparse.ArgumentParser()
# Positional argument（給參數時會依照順序填入，如果沒有提供會報錯）
# 使用 type = 可以指定要轉換成什麼樣的型態（預設是字串）
# help = 可以指定使用 -h 印出幫助訊息時，針對該參數顯示的說明
parser.add_argument('square', help="display a square of a give number", type=int)

# Opetional arguments（可以提供可以不提供的參數，也可以接收值）
# action='store_true' 自動存為 True or False
parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
parser.add_argument('-c', '--cube', help='display a cube of a give number', type=int)

# 解析參數並取得結果
args = parser.parse_args()

# 使用參數結果物件
print('square result = ' + str(args.square**2))

if args.verbose:
    print("verbosity turned on")

if args.cube:
    print('cube result = ' + str(args.cube**3))
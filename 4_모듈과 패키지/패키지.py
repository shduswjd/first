# import travel.thailand # travel같은 폴더 뒤에는 module 이나 package만 가능
# # 클래스나 함수는 import 불가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from은 가능함 
# # travel 폴더에 thailand.py 파일에서 ThailandPackage 클래스 호출
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from ~ import *
from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()
# 에러가 남
# __init__.py 파일에서 __all__썼더니 잘 나옴

# 패키지, 모듈 위치확인하기
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))


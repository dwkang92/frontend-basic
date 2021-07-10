from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete

# 1. Insert
# doc = {'name':'kyle','age': 17}
# # users라는 곳에 아래 doc이라는 변수를 insert_one한다.
# db.users.insert_one(doc)

# 2. Find
# 표 안의 id갑은 자동생성되어지는데, 그걸 표시하지말라는 명령도 꼭 넣어줘야한다.
# 해당 코드에서 find(조건}으로, 찾고싶은 조건들을 넣어준다. 없는경우,즉, 모든 document 데이터를 가져와라 => 빈칸으로 둔다.
# same_ages = list(db.users.find({'age':21},{'_id':False}))
# 모든조건을 다 가져와라.
# same_ages = list(db.users.find({},{'_id':False}))
#
# for person in same_ages:
#     print(same_ages)

# 3. Find_one
# MongoDB의 users 라는 이름의 collections에 저장된 모든 정보를 가져와라. 단, id값은 불필요.
# 그 다음, user정보의 나이들을 모두 불러와라.
# user = db.users.find_one({},{'_id': False})
# print(user['age'])

# 4. Update_one
# 이미 저장되어진 데이터값을 변경하는 역할.
# 이름이 booby인 데이터를 19살로 변경하라.
db.users.update_one({'name':'캐빈'},{'$set':{'age':19}})

# 5. delete_one
# 저장되어있는 데이터를 삭제하는 역할
# 이름이 bobby인 데이터를 삭제하여라.
db.users.delete_one({'name':'bobby'})
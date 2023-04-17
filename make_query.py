# 라이브러리 import
import json
import requests

# 고를 문제의 개수를 지정
problem_num = 8

# 리스트 선언
member_list = []
target_member_list = []
difficulty_list = []

# 멤버 리스트가 저장된 파일에서 멤버 리스트를 불러옴
file = open("data/KPSC_member_list.txt", 'r')
for i in file:
    member_list.append(i)
file.close()

# 문제별 타겟 멤버의 시작이 저장된 파일을 불러옴
file = open("data/ban_member.txt", 'r')
for i in file:
    target_member_list.append(int(i))
file.close()

# 문제별 난이도가 저장된 파일을 불러옴
file = open("data/difficulty.txt", 'r')
for i in file:
    difficulty_list.append(i)
file.close()

# 리스트에서 '\n' 삭제
for i in range(len(member_list)):
    member_list[i] = member_list[i][:-1]
for i in range(problem_num):
    difficulty_list[i] = difficulty_list[i][:-1]

for i in range(problem_num):
    # 문제를 랜덤으로 검색할 쿼리를 작성
    # 조건 1: 100명 이상이 푼 한국어 지문이 있는 문제
    # 조건 2: 난이도가 difficulty_list[i]인 문제
    problem_search_query = "s%23100..%26lang%3Ako" + "%26*" + difficulty_list[i]

    # 조건 3: (target_member_list[i]명부터 20명)이 안 푼 문제
    for j in range(target_member_list[i], min(target_member_list[i] + 20, len(member_list))):
        problem_search_query += "%26%21s%40" + member_list[j]

    # solved.ac api에 쿼리를 요청
    api_url = f"https://solved.ac/api/v3/search/problem?query={problem_search_query}&sort=random"
    query_result = requests.get(api_url)

    # 쿼리의 결과가 정상적으로 출력됐으면 랜덤으로 문제 하나를 출력
    if query_result.status_code == requests.codes.ok:
        query_json = json.loads(query_result.content.decode('utf-8'))

        random_problem_id = query_json.get("items")[0].get("problemId")

        print("problem count: " + str(query_json.get("count")) + ", problem id: " + str(random_problem_id))
    else:
        print("요청 실패")
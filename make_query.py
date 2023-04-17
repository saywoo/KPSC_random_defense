# 라이브러리 import
import json
import requests

# 멤버 리스트가 저장된 파일을 불러옴
member_file = open("data/KPSC_member_list.txt", 'r')

# 파일에서 멤버 리스트를 불러오고 푼 문제 순으로 정렬함
member_list = member_file.readlines()
member_file.close()

# 멤버 리스트에서 '\n' 제거
for i, member in enumerate(member_list):
    member_list[i] = member.strip('\n')

for problem_num in range(8):
    # 문제를 랜덤으로 검색할 쿼리를 작성
    # 기본조건: 100명 이상이 푼 한국어 지문이 있는 문제
    problem_search_query = "s#100..&lang:ko"

    # 모든 멤버가 풀지 않은 문제
    for i, member in enumerate(member_list):
        problem_search_query += "&!s@" + member

    api_url = f"https://solved.ac/api/v3/search/problem?query={problem_search_query}&sort=random&direction=desc"

    print(problem_search_query)



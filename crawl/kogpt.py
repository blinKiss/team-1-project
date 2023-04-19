# coding=utf8
# REST API 호출에 필요한 라이브러리
import requests
import json

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
REST_API_KEY = '85bc068140e59bad66c1c1de7a5e53cd'

# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
def kogpt_api(prompt, max_tokens = 1, temperature = 1.0, top_p = 1.0, n = 1):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        },
        headers = {
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

keyword = '꿀잼'
# KoGPT에게 전달할 명령어 구성
# prompt=f'{keyword} 긍정적인지 부정적인지:'
prompt = f'''
문장:{keyword}
문장이 긍정적인가요 부정적인가요?
답변:
'''

response = kogpt_api(prompt, max_tokens=32, temperature=0.3, top_p=0.85)

# prompt= "인간처럼 생각하고, 행동하는 '지능'을 통해 인류가 이제까지 풀지 못했던"
# response = kogpt_api(prompt, max_tokens=64, temperature=0.7, top_p=0.8)
print(response)
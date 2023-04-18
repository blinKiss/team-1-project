url = "https://search.pstatic.net/common?src=https%3A%2F%2Fmusicmeta-phinf.pstatic.net%2Falbum%2F009%2F334%2F9334427.jpg%3Ftype%3Dr204Fll%26v%3D20230413095719&type=os121_121"

# ".jpg" 이후의 문자열 위치를 찾습니다.
index = url.find(".jpg")

# ".jpg" 이후의 문자열을 제거합니다.
result = url[:index+4]

print(result)
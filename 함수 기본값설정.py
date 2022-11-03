'''def identiti(name, age, main_lang):
    print("이름 : {0}\t나이{1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))    # 문장이 실질적으로 한 줄로 인식됨


identiti("브루스", 26, "Rust")
identiti("madhatter", 52, "Java")
#출력
# 이름 : 브루스   나이26  주 사용 언어: Rust
# 이름 : madhatter        나이52  주 사용 언어: Java이름 : madhatter        나이52  주 사용 언어: Java
 '''


def identiti(name, age=15, main_lang="rust"):
    print("이름 : {0}\t나이{1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))    # 문장이 실질적으로 한 줄로 인식됨


identiti("Richerd")
identiti('Timorhy')
# 이름 : Richerd  나이15  주 사용 언어: rust
# 이름 : Timorhy  나이15  주 사용 언어: rust

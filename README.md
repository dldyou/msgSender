# BOJ 알림 메시지 보내기
https://foss4g.tistory.com/1624 참고
## Kakao Developers 설정

1. [Kakao Developers](https://developers.kakao.com/)에 접속 
2. 내 애플리케이션에서 애플리케이션 추가하기
3. 카카오 로그인 > 활성화 > Redirect URL 입력 (`https://localhost:8000`)
4. 동의항목 > 카카오톡 메시지 전송 > 이용 중 동의
5. 플랫폼 > 웹 > `https://www.google.co.kr` 등록
6. 구글 크롬 기준, 새 시크릿 창 > `https://kauth.kakao.com/oauth/authorize?client_id={REST API}&redirect_uri=https://localhost:8000&response_type=code&scope=talk_message,friends` > `https://localhost:8000/?code={code}` > `code 부분 복사하기`

## 참고 사이트
[메시지 템플릿](https://developers.kakao.com/docs/latest/ko/message/message-template)

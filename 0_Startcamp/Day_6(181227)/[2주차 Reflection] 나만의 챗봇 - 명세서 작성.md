서울 3반 이원진 https://github.com/Terpe66/TIL/tree/master/Startcamp/Day_6(181227)



### Lotto Check Bot : 당신은 돈을 날렸습니다



### 스펙

- 로또 회차와 번호를 입력 받아서 해당 회차의 당첨 여부와 등수를 확인합니다.
- 사용자가 /lotto 로 요청을 보냅니다.
- 체크할 회차와 번호를 입력할 html을 응답합니다.
- 사용자가 회차와 번호를 입력합니다.
- /lotto에서 입력받은 회차의 당첨번호와 보너스 번호, 사용자의 번호, 등수를 Telegram 메시지로 보냅니다.



### 회고

- 로또 당첨 번호 확인은 telegram 메시지가 없을 때는 1초 내외로 결과 페이지가 나타나는데 메시지 전송을 추가하면서 4초 내외까지 지연되는 문제가 발생함
- 시간 측정을 했을 때 크롤링이나 페이지로 넘기는 시간은 오래 걸리지 않는데 메시지를 보내는 게 오래 걸리는 걸 확인했지만, c9가 원인인지 우회해서 전송하는 게 원인인지 몰라서 방법을 알아봄



### 보완 계획

- 완료
- html, css 적용
- 포트폴리오 페이지에 개념 

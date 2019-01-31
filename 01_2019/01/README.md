# workshop homework 제출 양식

모든 workshop 과 homework 는`<MY-NAME>` 디렉토리 안에 디렉토리 별로 나눠서 제출!

| day  | workshop                              | homework          |
| ---- | ------------------------------------- | ----------------- |
| 03   | `workshop03/classroom/classmates.txt` | `homework03.txt`  |
| 04   | `workshop04.py`                       | `homework04.py`   |
| 05   | `workshop05.py`                       | `homework05.py`   |
| 06   | `workshop06.py`                       | `homework07.py`   |
| 07   | `workshop07.py`                       | `homework07.py`   |
| 08   | `workshop08.py`                       | `homework08.py`   |
| 09   | `workshop09.html`                     | `homework09.html` |
| 10   | `workshop10.html`                     | `homework10.txt`  |
| 11   | `workshop11.html`                     | `homework11.html` |
| 12   | `workshop12.html`                     | `homework12.txt`  |
| 14   | `workshop14/first_workshop/...`       | `homework14.txt`  |
| 15   | `workshop15.sql`                      | `homework15.txt`  |
| 16   | `workshop16.sql`                      | `homework16.sql`  |
| 17   | `workshop17/...`(app)                 | `homework17.py`   |
| 19   | `workshop19/...`(app)                 | homework19.md     |





## chocolatey / python 3.6.7 / Git / Chrome

1. windows cmd 를 관리자권한 로 열기.

2. chocolatey 설치

   1. https://chocolatey.org/install 에서 Install with cmd.exe 부분의 커맨드를 cmd 에 copy-paste (아래 명령어)

      ```sh
      > @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
      ```

   2. 설치가 완료되면, `> choco --version` 을 통해 버전 나오는 걸 확인

   3. `> choco search <package-name>` 가령 `choco search firefox` 같이 설치하려는 프로그램 검색 / https://chocolatey.org/packages 에서 검색

3. Python 설치 (chocolatey)

   1. `> choco install python --version 3.6.7`
   2. `> refreshenv`
   3. `> python --version` 을 통해 버전 확인

4. Git 설치 (chocolatey)

   1. `> choco install git -y`
   2. `> refreshenv`
   3. `> git --version` 으로 설치 확인

5. chrome 설치 (chocolatey)

   1. `> choco install GoogleChrome -y`

6. Typora 설치 (chocolatey)

   1. `> choco install typora -y`

7. Visual Studio code(Editor) 설치 (chocolatey)

   1. `> choco install vscode -y`


## `pip`

1. cmd 에서 계속 진행
2. 필요한 패키지들 설치
   1. `> pip install jupyter`

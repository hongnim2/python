# python
1. package 설치
  1.1. pycharm setting > project interpreter에서 cython, setuptools 설치

2. PyCharm에 File Type 추가
https://geoexamples.com/python/2017/04/20/pycharm-cython.html#:~:text=Compiling%20the%20cython%20file&text=Open%20File%2D%3ESettings%2D%3E,name%20at%20the%20project%20pane.
  2.1. File->Settings->Editor->File Types에서 Add Recognized File Types
    Name: Cython
    Cython files: Cython files
    Line comment: #
    Block comment start/end: '''
    Keywords #1: cdef, cpdef, cimport, ctypedef, def, for, if, import, return, while
  2.2. Add File Name Patterns
    *.pyx, *.pyd

3. setup.py 생성 및 설정
  3.1. Tools->create setup.py
  3.2. setup.py 수정
    from Cython.Build import cythonize
    
    setup(
      ext_modules = cythonize("helloworld.pyx")
    )

4. External Tool 설정
  4.1. File->Settings->Tools->External Tools에서  add
    Name: cython compile
    Description: Compile the cython files
    Program: python
    Arguments: setup.py build_ext --inplace
    Working directory: $ProjectFileDir$
    Advanced options: all check
    
5. MinGW 설치
https://cython.readthedocs.io/en/latest/src/tutorial/appendix.html
  5.1. 설치파일 다운로드
  5.2. Basic Package만 설치
  5.3. MSVC Build Tool 설치
    
----------------------------------------------------------------------------------------

# python
1. anaconda3 최신 설치
https://www.runnablecode.com/category/SW/Lang%20%7C%20Python
  1.1. 설치경로 확인 : C:\Users\<사용자명>\Anaconda3
  1.2. 나머지는 default로 next 연타
  1.3. 시스템 환경변수 Path에 "아나콘다경로\Library\bin" 추가
    C:\Users\HQWE201612002\Anaconda3
    C:\Users\HQWE201612002\Anaconda3\Library\bin
    C:\Users\HQWE201612002\Anaconda3\Scripts
    
2. pycharm for anaconda3 community버전 설치
https://bradbury.tistory.com/63?category=830131
  2.1. 설치까지만 진행. 설정은 5번에서 진행예정
  
3. envs 생성
https://bradbury.tistory.com/62
  3.1. anaconda3 prompt 실행
  3.2. anaconda3 업데이트
  https://kuduz.tistory.com/1171
    3.2.1. anaconda3 : conda update -n base conda
    3.2.2. anaconda3 패키지 : conda update --all
    3.2.3. pip : python -m pip install --upgrade pip
  3.3. conda list 입력 후, python 버전 확인
  3.4. envs 생성
    3.4.1. conda create -n 가상환경이름 python=버전
      ex> conda create -n python382 python=3.8.2
      
4. pyqt 설치
  4.1. anaconda3 prompt 실행
  4.2. envs 활성화
    activate python382
  4.3. pyqt설치
    pip install pyqt5
    
5. pycharm setting > project interpreter > add > conda environment > existing environment 선택
  5.1. interpreter 경로에 anaconda3 envs 경로+python.exe 입력
    ex> C:\Users\HQWE201612002\Anaconda3\envs\python38\python.exe
  5.2. 모든 프로젝트 적용 선택
  5.3. CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/current_repodata.json> 에러 발생 시,
    5.3.1. "아나콘다경로/Library/bin/" 경로 열기
    5.3.2. 다음 네 가지 파일들을 복사
      libcrypto-1_1-x64.dll
      libcrypto-1_1-x64.pdb
      libssl-1_1-x64.dll
      libssl-1_1-x64.pdb
    5.3.3. "아나콘다경로/DLLs/" 경로에 붙여넣기

6. package 설치
  6.1. pycharm setting > project interpreter에서 원하는 package 설치
  6.2. 추천항목
    pandas
    pyinstaller
    xlwings
    openpyxl
    pyserial

7. pysvn 설치
https://stackoverflow.com/questions/8941706/pysvn-installer-fails-to-detect-python-installation
  7.1. pysvn은 pip 미지원 모듈이라 별도 설치파일로 설치 필요
  https://pysvn.sourceforge.io/downloads.html
  7.2. 특정 env에 설치 방법
    7.2.1. regedit
    7.2.2. HKEY_LOCAL_MACHINE\SOFTWARE\Python\PythonCore\<설치된 파이썬 버전>\InstallPath 값 변경
      ex> C:\Users\HQWE201612002\Anaconda3\envs\python38
    7.2.3. pysvn 설치
    7.2.4. 레지스트리값 복원
      ex> C:\Users\HQWE201612002\AppData\Local\Programs\Python\Python38


------------------------------------------------------------------------------------

# python
python_lesson

1. install anaconda3 for python from https://www.anaconda.com/distribution/
2. make short-cut of jupyter Notebook on desktop
3. edit made short-cut as below
[As-Is]C:\Users\vgg\Anaconda3\python.exe C:\Users\vgg\Anaconda3\cwp.py C:\Users\vgg\Anaconda3 C:\Users\vgg\Anaconda3\python.exe C:\Users\vgg\Anaconda3\Scripts\jupyter-notebook-script.py "%USERPROFILE%/"
[To-Be]C:\Users\vgg\Anaconda3\python.exe C:\Users\vgg\Anaconda3\cwp.py C:\Users\vgg\Anaconda3 C:\Users\vgg\Anaconda3\python.exe C:\Users\vgg\Anaconda3\Scripts\jupyter-notebook-script.py "[TARGET_FOLDER]"
ex> C:\Users\vgg\Anaconda3\python.exe C:\Users\vgg\Anaconda3\cwp.py C:\Users\vgg\Anaconda3 C:\Users\vgg\Anaconda3\python.exe C:\Users\vgg\Anaconda3\Scripts\jupyter-notebook-script.py "D:\python_work"
4. laurnch made short-cut



hint.
if you want to know the detail information about functions,
position the cursor on the function and press "shift+Tab"

class MatrixCalculator:
    def __init__ (self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)] # 2차원 배열 생성 후 0으로 초기화 (리스트 컴프리헨션)
        self.update_matrix_properties() # 행렬 속성 초기화

    # 행렬 속성 업데이트
    def update_matrix_properties(self):
        self.diagnol = min(self.rows, self.cols) # 주대각선 크기
        self.main_diagnol = [self.matrix[i][i] for i in range(self.diagnol)] # 주대각성분 추출
        self.square_matrix = (self.rows == self.cols) # 정사각행렬 여부
        self.zero_matrix = all(self.matrix[r][c] == 0 for r in range(self.rows) for c in range(self.cols)) # 영행렬 여부
        self.lower_zero = True # 주대각선 아래가 모두 0인지 여부 
        for r in range (1, self.rows):
            for c in range (self.cols-1):
                if (r <= c):
                    break
                else:
                    if (self.matrix[r][c] != 0):
                        self.lower_zero = False
                # print(f"r={r}, c={c}, rows={self.rows}, cols={self.cols}, value={self.matrix[r][c]}")
        self.upper_zero = True # 주대각선 위가 모두 0인지 여부
        for r in range (self.rows-1):
            for c in range (1, self.cols):
                if (r >= c):
                    break
                else:
                    if (self.matrix[r][c] != 0):
                        self.upper_zero = False
        # 단위행렬 여부
        self.identity_matrix = False
        if (self.lower_zero and self.upper_zero and self.square_matrix and self.main_diagnol.count(1) == self.diagnol):
            self.identity_matrix = True

    # 성분 출력
    def print_entry(self, entry):
        if (isinstance(entry, int)): # 정수이고 int형일 때
            print(entry, end="")
        elif (isinstance(entry, float) and entry.is_integer()): # 정수인데 float형일 때
            print(f"{int(entry)}", end="") # 소수점 출력 x
        else: # 실수일 때
            print(entry, end="")

    # 행렬 출력
    def print_matrix(self):
        self.update_matrix_properties() # 행렬 속성 업데이트
        print_line() # 구분선 출력
        for r in range (self.rows):
            print("[", end="")
            for c in range (self.cols):
                self.print_entry(self.matrix[r][c])
                if (c < self.cols-1):
                    print("\t", end="")
            print("]")
        print(f"- 행렬 크기: {rows} x {cols}")
        print(f"- 정사각행렬 여부: {self.square_matrix}")
        print(f"- 영행렬 여부: {self.zero_matrix}")
        print(f"- 주대각성분: {self.main_diagnol}")
        print(f"- 상삼각행렬 여부: {self.lower_zero}")
        print(f"- 하삼각행렬 여부: {self.upper_zero}")
        print(f"- 단위행렬 여부: {self.identity_matrix}")
    
    # 행 번호 입력 함수 (유효한 행 번호 검사)
    """다른 함수에 적용하도록 변경 필요"""
    """다른 함수에서 row_num-1 지우고 여기에서 row_num-1 처리하도록 수정필요 (col_num도)"""
    def get_row_num(self, prompt: str):
        while (True):
            try:
                row_num = int(input(prompt))
                if (1 <= row_num <= self.rows):
                    return row_num
                else:
                    print("존재하지 않는 행 번호입니다. 다시 입력해 주세요.")
            except ValueError: # ValueError: 자료형과 다른 값 입력 시
                print("숫자만 입력해주세요.")
    
    # 열 번호 입력 함수 (유효한 열 번호 검사)
    """다른 함수에 적용하도록 변경 필요"""
    def get_col_num(self, prompt: str):
        while (True):
            try:
                col_num = int(input(prompt))
                if (1 <= col_num <= self.cols):
                    return col_num
                else:
                    print("존재하지 않는 열 번호입니다. 다시 입력해 주세요.")
            except ValueError:
                print("숫자만 입력해주세요.")
    
    # 행, 열 번호 입력 함수
    """다른 함수에 적용하도록 변경 필요"""
    def get_index_num(self, prompt: str):
        while (True):
            try:
                row_num, col_num = map(int, input(prompt).split())
                if (row_num >= 1 and col_num >= 1):
                    row_num -= 1
                    col_num -= 1
                    return row_num, col_num
                else:
                    print("1 이상의 정수만 입력해 주세요.")
            except ValueError:
                print("잘못 입력했습니다. 숫자 2개만 입력해 주세요.")

    # 성분 바꾸기
    def change_entry(self):
        print_line() # 구분선 출력
        print("***** 성분 1개 변경 *****")
        row_num, col_num = self.get_index_num("바꾸려는 성분의 행, 열 번호: ")
        value = int(input("바꿔 넣을 값을 입력하세요: "))
        self.matrix[row_num][col_num] = value
        self.print_matrix()
    
    # 행 바꾸기
    def change_row(self):
        print_line() # 구분선 출력
        print("***** 행 성분 변경 *****")
        self.row_num = self.get_row_num("바꿀 행 번호를 입력하세요: ")
        self.changed_row = input("행을 입력하세요: ").split()
        for i in range (self.cols):
            self.matrix[self.row_num-1][i] = int(self.changed_row[i])
        self.print_matrix()

    # 열 바꾸기
    def change_col(self):
        print_line()
        print("***** 열 성분 변경 *****")
        self.col_num = int(input("바꿀 열 번호를 입력하세요:"))
        self.changed_col = input("열을 입력하세요: ").split()
        for i in range (self.rows):
            self.matrix[i][self.col_num-1] = int(self.changed_col[i])
        self.print_matrix()
    
    # 행렬 전체에 스칼라 곱
    def scalar_multiplication(self):
        print_line() # 구분선 출력
        print("***** 행렬 실수곱 *****")
        self.value = float(input("행렬에 곱할 실수를 입력하세요: "))
        for c in range (self.cols):
            for r in range (self.rows):
                self.matrix[r][c] = self.matrix[r][c] * self.value
        self.print_matrix()
    
    # 한 행에 실수배
    def row_scalar_mul(self):
        print_line()
        print("****** 행에 실수 곱하기 *****")
        row_num = self.get_row_num("실수를 곱할 행 번호를 입력하세요: ")
        value = float(input("곱할 실수를 입력하세요: "))
        for i in range (self.cols):
            self.matrix[row_num-1][i] *= value
        self.print_matrix()

    # 스칼라 곱 후에 다른 행에 더하기
    def scalar_mul_and_addition(self):
        print_line()
        print("***** 행에 실수 곱해서 다른 행에 더하기 *****")
        self.mul_row_num = self.get_row_num("실수를 곱할 행 번호를 입력하세요: ")
        value = float(input("곱할 실수를 입력하세요: "))
        while (True):
            self.add_row_num = self.get_row_num("곱한 행을 더할 행 번호를 입력하세요: ")
            if (self.add_row_num == self.mul_row_num):
                print(f"같은 행에 더할 수 없습니다. {self.mul_row_num}행 외에 다른 행을 선택해 주세요")
            else:
                break
        for i in range (self.cols):
           self.matrix[self.add_row_num-1][i] += self.matrix[self.mul_row_num-1][i] * value
        self.print_matrix()
    
    # 행 교환하기
    def interchange_row(self):
        print_line() # 구분선 출력
        print("***** 행 교환 *****")
        self.temp = input("교환할 두 행의 번호를 입력하세요: ").split()
        self.interchange_row_num = [0 for _ in range(2)]
        for i in range (2):
            self.interchange_row_num[i] = int(self.temp[i])-1
        self.temp_row = self.matrix[self.interchange_row_num[0]]
        self.matrix[self.interchange_row_num[0]] = self.matrix[self.interchange_row_num[1]]
        self.matrix[self.interchange_row_num[1]] = self.temp_row
        self.print_matrix()
        
# 구분선 출력
def print_line():
    print("-" * 50)

# 계산기 실행
def run_calculator():
    while (True):
        print_line() # 구분선 출력
        print("cr: 행 성분 변경 | cc: 열 성분 변경 | c: 성분 1개 변경 | ir: 행 교환 | rm: 한 행에 실수곱 | ma: 실수곱+더하기 | m: 행렬 실수곱 | q: 종료")
        option = input("수행할 연산을 선택하세요: ")
        if (option == "c"): # 성분 바꾸기
            calc1.change_entry()
        elif (option == "m"): # 행렬 실수곱
            calc1.scalar_multiplication()
        elif (option == "cr"): # 행 바꾸기
            calc1.change_row() 
        elif (option == "cc"): # 열 바꾸기
            calc1.change_col()
        elif (option == "ir"): # 행 교환
            calc1.interchange_row()
        elif (option == "ma"): # 행에 실수곱 후 다른 행에 더함
            calc1.scalar_mul_and_addition()
        elif (option == "rm"): # 행 실수곱
            calc1.row_scalar_mul()
        elif (option == "q"): # 종료
            return 0
        else:
            print("※ 잘못 입력하셨습니다. 다시 입력하세요")

            

##### 실행 부분 #####
while (True):
    try:
        rows, cols = map(int, input("행렬의 크기 입력(예: a b → a * b 크기 행렬): ").split())
        if (rows >= 1 and cols >= 1):
            break
    except ValueError:
        print("숫자만 입력해 주세요.")

calc1 = MatrixCalculator(rows, cols)
calc1.print_matrix()
run_calculator()
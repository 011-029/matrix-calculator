class MatrixCalculator:
    def __init__ (self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)] # 2차원 배열 생성 (리스트 컴프리헨션)
        self.update_matrix_properties() # 행렬 속성 초기화

    # 행렬 속성 업데이트
    def update_matrix_properties(self):
        self.diagnol = min(self.rows, self.cols) # 주대각선 크기
        self.main_diagnol = [self.matrix[i][i] for i in range(self.diagnol)] # 주대각성분 추출
        self.square_matrix = (self.rows == self.cols) # 정사각행렬 여부
        self.zero_matrix = all(self.matrix[r][c] == 0 for r in range(self.rows) for c in range(self.cols)) # 영행렬 여부
        """단위행렬, 삼각행렬 여부 추가하기"""
    
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
        # for i in range (self.rows):
            # self.print_entry(self.matrix[i])
            # print(self.matrix[i])
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

    # 성분 바꾸기
    def change_entry(self):
        print_line() # 구분선 출력
        print("***** 성분 바꾸기 *****")
        self.index = input("바꾸려는 성분의 행, 열 번호: ").split()
        self.value = int(input("바꿔 넣을 값을 입력하세요: "))
        self.matrix[int(self.index[0]) - 1][int(self.index[1]) - 1] = self.value
        self.print_matrix()
    
    # 행 바꾸기
    def change_row(self):
        print_line() # 구분선 출력
        print("***** 행 바꾸기 *****")
        self.row_num = int(input("바꿀 행 번호를 입력하세요: "))
        self.changed_row = input("행을 입력하세요: ").split()
        for i in range (self.cols):
            self.matrix[self.row_num-1][i] = int(self.changed_row[i])
        self.print_matrix()

    # 열 바꾸기
    def change_col(self):
        print_line()
        print("***** 열 바꾸기 *****")
        self.col_num = int(input("바꿀 열 번호를 입력하세요:"))
        self.changed_col = input("열을 입력하세요: ").split()
        for i in range (self.rows):
            self.matrix[i][self.col_num-1] = int(self.changed_col[i])
        self.print_matrix()
    
    # 행렬 스칼라 곱
    def scalar_multiplication(self):
        print_line() # 구분선 출력
        print("***** 행렬 실수곱 *****")
        self.value = float(input("행렬에 곱할 실수를 입력하세요: "))
        for c in range (self.cols):
            for r in range (self.rows):
                self.matrix[r][c] = self.matrix[r][c] * self.value
        self.print_matrix()
        
def print_line():
    print("-" * 50)

def run_calculator():
    while (True):
        print_line() # 구분선 출력
        print("cr: 행 바꾸기 | cc: 열 바꾸기 | c: 성분 바꾸기 | m: 행렬 실수곱 | q: 종료")
        option = input("수행할 연산을 선택하세요: ")
        if (option == "c"): # 성분 바꾸기
            calc1.change_entry()
        elif (option == "m"): # 행렬 실수곱
            calc1.scalar_multiplication()
        elif (option == "cr"): # 행 바꾸기
            calc1.change_row() 
        elif (option == "cc"): # 열 바꾸기
            calc1.change_col()
        elif (option == "q"): # 종료
            return 0
        else:
            print("※ 잘못 입력하셨습니다. 다시 입력하세요")
        
index = input("행렬의 크기 입력(예: a b → a * b 크기 행렬): ").split()
rows, cols = int(index[0]), int(index[1])
calc1 = MatrixCalculator(rows, cols)
calc1.print_matrix()
run_calculator()
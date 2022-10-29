#coding=GBK
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ###��ϣ��ķ�ʽ����¼ÿ��ÿ�м�ÿ���Ź���ÿ�����ֳ��ֵĴ���
        rows=[[0]*9 for _ in range(9)]
        columns=[[0]*9 for _ in range(9)]
        subboxes=[[[0]*9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                c=board[i][j]
                if c!='.':
                    idx=ord(c)-ord('0')-1
                    rows[i][idx]+=1
                    columns[j][idx]+=1
                    subboxes[i//3][j//3][idx]+=1
                    if rows[i][idx]>1 or columns[j][idx]>1 or subboxes[i//3][j//3][idx]>1:
                        # print(c,i,j,idx)
                        return False
        return True
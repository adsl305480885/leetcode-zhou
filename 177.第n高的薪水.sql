--
-- @lc app=leetcode.cn id=177 lang=mysql
--
-- [177] 第N高的薪水
--

-- @lc code=start
CREATE FUNCTION getNthHighestSalary(N  INT)  RETURNS INT


BEGIN
    DECLARE M INT;
	SET M = N - 1;
	RETURN (
	
		-- limit m,n    : 意思是跳过m个记录向后取n条数据。
		-- distinct 去掉重复项目
		-- desc从高到底，降序排序
		SELECT DISTINCT salary FROM employee ORDER BY salary DESC LIMIT M, 1
	);
END


-- @lc code=end


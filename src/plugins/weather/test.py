from utils import Robot

robot = Robot()
# issue = robot.create_issue("测试话题")
stripped_arg = "12 哈哈哈这是对的 测试"
content = stripped_arg.split()
print(content)
issue_number = int(content[0])
comment_content = " ".join(content[1:]) 
comment = robot.create_comment_by_issue_number(issue_number,comment_content)

print('OK')
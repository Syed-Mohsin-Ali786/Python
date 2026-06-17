# class Post:
#     def __init__(self, title: str, description: str):
#         self.title = title
#         self.description = description
        
#         print(f"Post created successfully!")
#         print(f" -> Title: {self.title}")
#         print(f" -> Description: {self.description}\n")


# # 1. The Raw Data
# post_data_dict = {
#     "title": "My First Post", 
#     "description": "Hello world"
# }

# print("--- Method 1: Using ** Unpacking ---")
# # This works perfectly because the Post class __init__ expects 'title' and 'description'
# post1 = Post(**post_data_dict)


# print("--- Method 2: Manual Keyword Arguments ---")
# post2 = Post(title="My First Post", description="Hello world")


# print("--- Verification Check ---")
# print(f"Are the titles identical? {post1.title == post2.title}")



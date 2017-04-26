from models.blog import Blog
from database import Database

class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        # Check is they've already got an account
        # If not, prompt to create one
        pass

    def _user_has_account(self):
        blog = Database.find_one('blogs',{'author':self.user})
        if blog is not None:
            ## assign an object!
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author = self.user,
                    title = title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read (r) or write (w) blogs? ").lower()
        if read_or_write.startswith('r'):
            self._list_blogs()
            self._view_blog()
            # if read:
            # list blogs in database
            # allow user to pick one
            # disply posts
            pass
        elif read_or_write.startswith('w'):
            self.user_blog.new_post()
        else:
            print("thank you for blogging!")

    def _prompt_write_post(self):
        self.user_blog.new_post()

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print ("ID: {}, Title: {}, Author: {}".format(
                blog['id'],
                blog['title'],
                blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the ID of the blog: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, title: {}\nby: {}\n\n{}".format(
                post['created_date'],
                post['title'],
                post['author'],
                post['content']
            ))
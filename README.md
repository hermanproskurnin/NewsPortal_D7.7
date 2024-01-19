Django Blog System

This Django project implements a simple blog system with features such as user authentication, article creation, and commenting. The application consists of several models representing authors, categories, posts, and comments.

Models:

1. Author
   - Linked to the built-in User model for authentication.
   - Contains the author's rating, which is calculated based on the rating of their posts and comments.

2. Category
   - Represents categories or topics for articles.
   - Ensures each category has a unique name.

3. Post
   - Represents individual blog posts or articles.
   - Belongs to an author and can be assigned multiple categories.
   - Supports different types (e.g., News or Article).
   - Includes a title, text, date of creation, and a rating.
   - Allows users to like or dislike posts to influence their ratings.

4. PostCategory (Intermediate Model)
   - Represents the many-to-many relationship between posts and categories.

5. Comment
   - Represents user comments on blog posts.
   - Associated with a specific post and user.
   - Includes text, date of creation, and a rating.
   - Supports liking or disliking comments.

Features:
- User authentication using Django's built-in User model.
- Creating, editing, and deleting blog posts with different types and categories.
- Liking or disliking posts and comments to influence their ratings.
- Preview method for a concise view of the post's content.
- User-specific pages to view their own posts and comments.

How to Use:
1. Clone the repository.
2. Run migrations using `python manage.py migrate` to set up the database.
3. Create a superuser using `python manage.py createsuperuser` to access the Django admin panel.
4. Run the development server using `python manage.py runserver`.
5. Access the admin panel at `http://localhost:8000/admin/` to manage authors, categories, posts, and comments.

Feel free to customize and extend the functionality to fit your blogging needs.

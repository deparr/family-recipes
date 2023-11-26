from flask import current_app as app

from repositories import PostRepository, CommentRepository
from dtos import PostDto, CommentDto
from dtos.responses import DataResponse, DeleteResponse, CreateResponse
from dtos.errors import BadRequestError


def validateNewPost(post: PostDto):
    badVal = None
    if post.author is None or len(post.author) == 0:
        badVal = "author"

    if post.recipeId is None:
        badVal = "recipeId"

    if post.groupId is None:
        badVal = "groupId"

    if badVal is not None:
        raise BadRequestError(f"Need post.{badVal} to create post")


def validateNewComment(comment: CommentDto):
    badVal = None
    if comment.author is None or len(comment.author) < 1:
        badVal = "author"

    if comment.postId is None or comment.postId < 1:
        badVal = "postId"

    if comment.content is None:
        badVal = "content"

    if badVal is not None:
        raise BadRequestError(f"Need valid comment.{badVal} to create comment")


class PostService:
    def __init__(self):
        self.postRepo = PostRepository()
        self.commentRepo = CommentRepository()

    def makePost(self, post: PostDto) -> CreateResponse:
        validateNewPost(post)
        app.logger.info(f"creating {post}...")
        insertedId = self.postRepo.insertPost(post)
        res = CreateResponse(201, insertedId)

        return res

    def getPost(self, id: int) -> DataResponse:
        post = self.postRepo.getPostById(id)
        res = DataResponse(200, post)

        return res

    def getUserPosts(self, username: str) -> DataResponse:
        posts = self.postRepo.getPostsByUser(username)
        res = DataResponse(200, posts)

        return res

    def getGroupPosts(self, groupId: int) -> DataResponse:
        posts = self.postRepo.getPostsByGroup(groupId)
        res = DataResponse(200, posts)

        return res

    def deletePost(self, id: int) -> DeleteResponse:
        rowsAffected = self.postRepo.deletePostById(id)
        res = DeleteResponse(200, rowsAffected)

        return res

    def makeComment(self, comment: CommentDto):
        validateNewComment(comment)
        insertedId = self.commentRepo.insertComment(
            comment.postId, comment.author, comment.content)

        return CreateResponse(201, insertedId)

    def getPostComments(self, postId: int) -> DataResponse:
        comments = self.commentRepo.getCommentsByPost(postId)
        res = DataResponse(200, comments)

        return res

    def deleteComment(self, id: int) -> DeleteResponse:
        rowsAffected: int = self.commentRepo.deleteComment(id)

        return DeleteResponse(200, rowsAffected)

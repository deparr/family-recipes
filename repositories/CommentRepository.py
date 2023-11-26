from libsql_client import ResultSet

from .BaseRepository import BaseRepository
from dtos import CommentDto


class CommentRepository(BaseRepository):
    INSERT_COMMENT = "insert into comment (author, content, post_id, created_at, edited) values (?,?,?,datetime(),0)"
    SELECT_ALL_BY_ID = "select * from comment where comment.id = ?"
    SELECT_ALL_BY_POST = "select * from comment where comment.post_id = ?"
    SELECT_ALL_BY_AUTHOR = "select * from comment where comment.author = ?"
    # TODO need to think about how to do updates or if we want to do them at all
    UPDATE_BY_ID = ""
    DELETE_BY_ID = "delete from comment where comment.id = ?"
    DELETE_BY_POST = "delete from comment where comment.post_id = ?"
    DELETE_BY_AUTHOR = "delete from comment where comment.author = ?"

    def __init__(self):
        super().__init__()

    def insertComment(self, postId: int, author: str, content: str) -> int:
        rs: ResultSet = self.execute(
            CommentRepository.INSERT_COMMENT,
            [author, content, postId])

        return rs.last_insert_rowid

    def getComment(self, id: int) -> CommentDto:
        rs: ResultSet = self.execute(
            CommentRepository.SELECT_ALL_BY_ID,
            [id])

        comment = CommentDto.fromResultSet(rs)
        return comment

    def getCommentsByPost(self, postId: int) -> list[CommentDto]:
        rs: ResultSet = self.execute(
            CommentRepository.SELECT_ALL_BY_POST,
            [postId])

        comments = CommentDto.fromResultSet(rs, forceArray=True)
        return comments

    def getCommentsByAuthor(self, author: str) -> list[CommentDto]:
        rs: ResultSet = self.execute(
            CommentRepository.SELECT_ALL_BY_AUTHOR,
            [author])

        comments = CommentDto.fromResultSet(rs, forceArray=True)
        return comments

    def deleteComment(self, id: int) -> int:
        rs: ResultSet = self.execute(
            CommentRepository.DELETE_BY_ID,
            [id])

        return rs.rows_affected

    def deletePostComments(self, postId: int) -> int:
        rs: ResultSet = self.execute(
            CommentRepository.DELETE_BY_POST,
            [postId])

        return rs.rows_affected

    def deleteAuthorComments(self, author: str) -> int:
        rs: ResultSet = self.execute(
            CommentRepository.DELETE_BY_AUTHOR,
            [author])

        return rs.rows_affected

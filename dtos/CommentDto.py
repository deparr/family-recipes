from libsql_client import ResultSet


class CommentDto(dict):
    def __init__(self, id, author, content, postId, dateCreated, edited):
        super().__init__(
            id=id,
            author=author,
            postId=postId,
            content=content,
            dateCreated=dateCreated,
            edited=edited
        )

    def fromJson(json: dict):
        return CommentDto(
            json.get("id"),
            json.get("author"),
            json.get("content"),
            json.get("postId"),
            json.get("dateCreated"),
            json.get("edited")
        )

    def fromResultSet(rs: ResultSet, forceArray=False):
        if len(rs) == 0:
            return None

        if len(rs) == 1 and not forceArray:
            row = rs[0]
            return CommentDto(
                row[0], row[1],
                row[2], row[3],
                row[4], row[5]
            )

        return [CommentDto(row[0], row[1], row[2], row[3], row[4], row[5])
                for row in rs]

    def __str__(self):
        return f"comment{super().__str__()}"

    def __getattr__(self, attr: str):
        return self[attr]

    def __setattr__(self, attr: str, value: any):
        self[attr] = value

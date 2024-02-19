from database.sqlite3.session import SqliteSession


class UserRepo:
    def __init__(self, session: SqliteSession):
        self.session = session

    def create(self, username: str, age: int) -> int | None:
        query = "INSERT INTO users (username, age) VALUES (?, ?)", (username, age)
        self.session.execute(*query)
        last_id = self.session.lastrowid()
        return last_id

    def get(self):  # ALL
        query = "SELECT * FROM users"
        self.session.execute(query)
        return self.session.fetchall()

    def get_by_id(self, id):  # By id
        query = "SELECT * FROM users WHERE id = ?", (id,)
        self.session.execute(*query)
        return self.session.fetchone()

    def _build_set_clause_and_params(self, **kwargs):  # noqa
        set_clause = []
        params = []

        for key, value in kwargs.items():
            set_clause.append(f"{key} = ?")
            params.append(value)
        set_clause = ", ".join(set_clause)

        return set_clause, params

    def update(self, id, **kwargs):
        clause, params = self._build_set_clause_and_params(**kwargs)
        query = f"UPDATE users SET {clause} WHERE id = ?", (*params, id)
        self.session.execute(*query)

    def delete(self, id):
        query = "DELETE FROM users WHERE id = ?", (id,)
        self.session.execute(*query)

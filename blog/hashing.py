from passlib.context import CryptContext


class Hash:
    pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcrypt(self, password):
        return Hash.pwd_ctx.hash(password)

    def verify(self, hashed_password, plain_password):
        return Hash.pwd_ctx.verify(plain_password, hashed_password)

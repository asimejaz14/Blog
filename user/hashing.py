from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


class Hash:

    @staticmethod
    def get_hash_password(plain_text):
        return pwd_context.hash(plain_text)

    @staticmethod
    def verify_password(plain_password, hash_password):
        return pwd_context.verify(plain_password, hash_password)

from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    descricao: Mapped[str] = mapped_column(String(100), nullable=False)
    preco: Mapped[float] = mapped_column(Float, nullable=False)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('users.id'))

    # backref cria o relacionamento bidirecional automaticamente
    usuario = relationship("User", backref=backref("produtos"))

from db.connection import db
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime, timezone
from sqlalchemy import DateTime




class Users(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    plan: Mapped[str] = mapped_column(default="free")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))

